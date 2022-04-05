from roku import Roku
import random

roku = Roku('10.10.100.124')

rand_commands = ['back', 'backspace', 'down', 'enter', 'forward', 'home',
                 'info', 'left', 'play', 'replay', 'reverse', 'right', 'search', 'select', 'up']
rand_series = ['Voltron in Space', 'shctf{T1m3-is-th3-ultimat3-curr3Ncy}',
               'Battlestar Galatica', 'Dune', 'Highlander', 'Star Wars', 'Star Trek', 'Treasure Planet']

for x in range(0, 200):
    roku.search()
    rand_show = rand_series[random.randint(0, len(rand_series)-1)]
    if (rand_show == 'shctf{T1m3-is-th3-ultimat3-curr3Ncy}'):
        print("<<< flag in traffic")
    roku.literal(rand_show)
