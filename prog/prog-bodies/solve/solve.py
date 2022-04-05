from pwn import *
import threading
import time
import sys
import os
from telnetlib import Telnet
import random


def ret_l(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'L= ')
    res = float(tn.read_very_lazy().split(b'\n')[0].strip(b' '))
    tn.write(b'\n')
    return res


def ret_adist(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'ADIST= ')
    res = float(tn.read_very_lazy().split(b'\n')[0].strip(b' '))
    tn.write(b'\n')
    return res


def ret_angmon(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'ANGMOM= ')
    res = float(tn.read_very_lazy().split(b'\n')[0].strip(b' '))
    tn.write(b'\n')
    return res


def ret_qr(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'QR= ')
    res = float(tn.read_very_lazy().split(b'TP=')[0].strip(b' '))
    tn.write(b'\n')
    return res


def ret_rms(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'RMS= ')
    res = float(tn.read_very_lazy().split(b'\n')[0].strip(b' '))
    tn.write(b'\n')
    return res


def ret_epoch(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'EPOCH= ')
    res = float(tn.read_very_lazy().split(b'!')[0].strip(b' '))
    tn.write(b'\n')
    return res


def step_prompt(step):
    sys.stdout.flush()


print("<<< Connecting to NASA... <please wait>")
tn = Telnet('horizons.jpl.nasa.gov', 6775)

context.timeout = 60
p = remote('0.cloud.chals.io', 24054)
#p = remote('localhost',3333)

print(p.recvline())
print(p.recvline())

for i in range(0, 5):
    req = p.recvuntil(b" >>>")
    req_stat = req.split(b"<")[1].split(b">")[0]
    req_body = req.split(b"for ")[1].strip(b" >>>")+b"\n"
    print("Solving for", req_stat, req_body)
    sys.stdout.flush()
    if req_stat == b"l":
        print("<<L>>")
        sol = ret_l(tn, req_body)
    elif req_stat == b"adist":
        print("<<ADIST>>")
        sol = ret_adist(tn, req_body)
    elif req_stat == b"angmon":
        print("ANGMON")
        sol = ret_angmon(tn, req_body)
    elif req_stat == b"qr":
        print("QR")
        sol = ret_qr(tn, req_body)
    elif req_stat == b"rms":
        print("RMS")
        sol = ret_rms(tn, req_body)
    elif req_stat == b"epoch":
        print("EPOCH")
        sol = ret_epoch(tn, req_body)
    sys.stdout.flush()
    print("Ans >>> ", sol)
    p.sendline(str(sol).encode())
    print(p.recvline())
p.interactive()
