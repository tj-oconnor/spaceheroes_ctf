from scapy.all import *

qwerty_map = {  # Pretty full map of a qwerty keyboard
    0: 'alt',
    1: 'esc',
    2: '1',
    3: '2',
    4: '3',
    5: '4',
    6: '5',
    7: '6',
    8: '7',
    9: '8',
    10: '9',
    11: '0',
    12: "-",
    13: '=',
    14: 'backspace',
    15: 'tab',
    16: 'q',
    17: 'w',
    18: 'e',
    19: 'r',
    20: 't',
    21: 'y',
    22: 'u',
    23: 'i',
    24: 'o',
    25: 'p',
    26: '[',
    27: ']',
    28: 'enter',
    29: 'control',
    30: 'a',
    31: 's',
    32: 'd',
    33: 'f',
    34: 'g',
    35: 'h',
    36: 'j',
    37: 'k',
    38: 'l',
    39: ';',
    40: "'",
    41: '`',
    42: 'shift',
    43: '\ ',
    44: 'z',
    45: 'x',
    46: 'c',
    47: 'v',
    48: 'b',
    49: 'n',
    50: 'm',
    51: ',',
    52: '.',
    53: '/',
    54: 'shift',
    56: 'alt',
    57: ' ',
    58: 'caps lock',
    97: 'control'}


pkts = rdpcap('strangetrafficchallenge.pcap')

for pkt in pkts:
    if pkt.haslayer('Raw'):
        x = (int(pkt[Raw].load.split(b' ')[5], 10))
        print(qwerty_map[x], end='')

# ignoring enter, and matching shifts to capital letters:shctf{thanks f0r th3 t4nk. he n3ver get5 me anyth1ng}
