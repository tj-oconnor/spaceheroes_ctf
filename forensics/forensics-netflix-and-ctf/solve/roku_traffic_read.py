from scapy.all import *
import sys

keys = b''
pkts = rdpcap(sys.argv[1])
for pkt in pkts:
    if pkt.haslayer('Raw'):
        if b'Lit_' in pkt['Raw'].load:
            keys += ((pkt['Raw'].load).split()[1]).split(b'_')[1]

flag = (keys.split(b'%7B')[1]).split(b'%7D')[0]
print('shctf{%s}' % flag.decode())
