from scapy.all import *
from sys import stdout
import random
# Several Conversation
# Scattered ICMP and one backwords not so scattered

# New_base_on_planet_hoth
# [123456789012345678901234567890123456789012345678901234567890] 51
# New [TCPSYN CONVO]
MessageOne = "[00:02]News lately suggest the rebels have made a new base[anonR1]"
# [1234567890123456789012345678901234567890123456789012345678901234567890] 64
# planet [ICMP Reverse Message]
MessageTwo = "[34:39]What? I doubt that, there is'nt a planet left they could hide in[anonE2]"
# [1234567890123456789012345678901234567890123456789012345678901234567890] 67
# on [TCPSYN Mimic]
MessageThree = "[03:04]I dont support the rebels, but they sure are brave to keep on going[anonB1]"
# [1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890] 90
# base [split into 7 ICMP]
MessageFour = "[49:52]BRAVE? you have to be kidding no matter how many bases they make, they will always be scum[anonE1]"
# [123456789012345678901234567890123456789012345678901234567890] 40
# hoth [UDP dest ports]
MessageFive = "[35:38]Hey man, theres no reason to be so hotheaded relax[anonL1]"

List = []
temp = ''
counter = 0

for i in MessageFour:

    #packet = IP(src="192.168.153.127",dst="123.12.1.13",id = ord(i))
    # write(packet)
    temp = temp + i

    counter += 1
    if counter == 15:
        List.append(temp)
        counter = 0
        temp = ''


def write(pkt):
    wrpcap('Challenge.pcap', pkt, append=True)


def UDPPort():
    for i in MessageFive:
        ran = random.randrange(20, 126)
        pkt = Ether()/IP(src="10.13.103.14", dst="102.1.1.13")/UDP(sport=ran, dport=ord(i))
        write(pkt)


def ICMPScatter(num):
    for i in List[num]:
        ran = random.randrange(1, 126)
        pkt = Ether()/IP(src="10.11.10.12", dst="101.12.1.132") / \
            ICMP(type=0, code=ord(i), seq=ran)
        write(pkt)


def TCPConvo():
    Src = random.randrange(1, 1000)
    Dest = random.randrange(1, 1000)
    for i in range(len(MessageOne)):

        if i % 2 == 0:
            pkt = Ether()/IP(src="107.13.12.154", dst="18.44.117.9") / \
                TCP(sport=Src, dport=Dest, seq=ord(MessageOne[i]))
        else:
            pkt = Ether()/IP(src="18.44.117.9", dst="107.13.12.154") / \
                TCP(sport=Dest, dport=Src, seq=ord(MessageOne[i]))
            Src = random.randrange(1, 1000)
            Dest = random.randrange(1, 1000)
        write(pkt)


def TCPMimic():
    for i in MessageThree:
        Src = random.randrange(1, 1000)
        Dest = random.randrange(1, 1000)
        pkt = Ether()/IP(src="99.7.1.15", dst="107.45.121.24") / \
            TCP(sport=Src, dport=Dest, seq=ord(i))
        pkt = Ether()/IP(src="107.45.121.24", dst="99.7.1.15") / \
            TCP(sport=Dest, dport=Src, seq=ord(i))
        write(pkt)


def ICMPReverse():
    for i in (MessageTwo[::-1]):
        ran = random.randrange(1, 126)
        pkt = Ether()/IP(src="18.15.102.18", dst="11.183.43.98") / \
            ICMP(type=0, code=ran, seq=ord(i))
        write(pkt)


def PrintJunk(num):
    ran = random.randrange(1, 6)

    if num == 0:
        for i in range(ran):
            Src = str(random.randrange(1, 127)) + '.'+str(random.randrange(1, 127)) + \
                '.'+str(random.randrange(1, 127))+'.' + \
                str(random.randrange(1, 127))
            Dest = str(random.randrange(1, 127)) + '.'+str(random.randrange(1, 127)) + \
                '.'+str(random.randrange(1, 127))+'.' + \
                str(random.randrange(1, 127))
            pkt = Ether()/IP(src=Src, dst=Dest)/UDP()/RTP()
            write(pkt)
    elif num == 1:
        for i in range(ran):
            Src = str(random.randrange(1, 127)) + '.'+str(random.randrange(1, 127)) + \
                '.'+str(random.randrange(1, 127))+'.' + \
                str(random.randrange(1, 127))
            Dest = str(random.randrange(1, 127)) + '.'+str(random.randrange(1, 127)) + \
                '.'+str(random.randrange(1, 127))+'.' + \
                str(random.randrange(1, 127))
            pkt = Ether()/IP(src=Src, dst=Dest)
            write(pkt)
    elif num == 2:
        for i in range(ran):
            Src = str(random.randrange(1, 127)) + '.'+str(random.randrange(1, 127)) + \
                '.'+str(random.randrange(1, 127))+'.' + \
                str(random.randrange(1, 127))
            Dest = str(random.randrange(1, 127)) + '.'+str(random.randrange(1, 127)) + \
                '.'+str(random.randrange(1, 127))+'.' + \
                str(random.randrange(1, 127))
            pkt = Ether()/IP(src=Src, dst=Dest)/UDP()/SNMP()
            write(pkt)


def PrintAll():
    PrintJunk(0)
    ICMPScatter(0)
    TCPMimic()
    ICMPScatter(1)
    PrintJunk(2)
    PrintJunk(1)
    ICMPScatter(2)
    UDPPort()
    ICMPScatter(3)
    TCPConvo()
    PrintJunk(1)
    ICMPScatter(4)
    ICMPReverse()
    ICMPScatter(5)
    PrintJunk(0)
    ICMPScatter(6)
    PrintJunk(2)


PrintAll()
