import angr
import claripy
import sys

def main(argv):
  path_to_binary = argv[1] 
  random_val = int(argv[2])

  project = angr.Project(path_to_binary)

  start_address = 0x401680
  initial_state = project.factory.blank_state(
    addr=start_address,
    add_options = { angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
                    angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS}
  )

  password0 = claripy.BVS('', 64)
  password1 = claripy.BVS('', 64)
  password2 = claripy.BVS('', 64)
  password3 = claripy.BVS('', 64)

  initial_state.regs.r9 = password0
  initial_state.regs.r10 = password1
  initial_state.regs.r11 = password2
  initial_state.regs.r12 = password3
  initial_state.regs.r13 = random_val

  simulation = project.factory.simgr(initial_state)

  def is_successful(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return 'Authentication Succeeded.'.encode() in stdout_output

  def should_abort(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return 'Authentication Failed.'.encode() in stdout_output

  simulation.explore(find=is_successful, avoid=should_abort)

  if simulation.found:
    solution_state = simulation.found[0]

    solution0 = solution_state.solver.eval(password0)
    solution1 = solution_state.solver.eval(password1)
    solution2 = solution_state.solver.eval(password2)
    solution3 = solution_state.solver.eval(password3)

    solution = ' '.join(map('{:x}'.format, [ solution0, solution1, solution2, solution3 ]))  
    print(solution)
  else:
    raise Exception('Could not find the solution')

if __name__ == '__main__':
  main(sys.argv)
