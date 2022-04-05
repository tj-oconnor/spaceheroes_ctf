from scapy.all import *
from scapy.utils import PcapWriter
import os
import base64
import random

'''
{15:57}~ ping www.starwars.com
PING a1996.dscf1.akamai.net (162.248.71.9): 56 data bytes

{15:57}~ ping www.startrek.com
PING ctd.cbsi.map.fastly.net (151.101.5.188): 56 data bytes
'''

src = "162.248.71.9"
dst = "151.101.5.188"

pcapF = PcapWriter("star.pcap", append=True, sync=True)


def make_icmp_flag(flag):
    for f in flag:
        pkt = Ether()/IP(src=src, dst=dst)/ICMP(type=0, code=ord(f))
        pcapF.write(pkt)


def test_encode():
    print("-------- building pcap -------------")
    flag = base64.b64encode(
        b"shctf{L0g1c-i$-th3-begiNNing-0f-wi$doM}").decode()
    make_icmp_flag(flag)


def test_decode():
    print("-------- asserting solution -------------")
    pkts = rdpcap('star.pcap')
    msg = ''
    for pkt in pkts:
        if (pkt['ICMP'].type == 0):
            msg += chr(pkt['ICMP'].code)
    print(base64.b64decode(msg))


test_encode()
test_decode()
