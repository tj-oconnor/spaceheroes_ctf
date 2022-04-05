from scapy.all import *
from scapy.utils import PcapWriter
import os
import base64
import random
import sys


def test_decode():
    pkts = rdpcap(sys.argv[1])
    msg = ''
    for pkt in pkts:
        if (pkt['ICMP'].type == 0):
            msg += chr(pkt['ICMP'].code)
    print(base64.b64decode(msg))


test_decode()
