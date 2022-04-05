from random import random, uniform
from pprint import pprint

TOTAL_STATS = 10
TOTAL_BATTLES = 25


ships = []
ships.append('Starfleet Assault Cruiser')
ships.append('Starfleet Assault Frigate')
ships.append('Starfleet Fast Scout')
ships.append('Starfleet Heavy Scout')
ships.append('Starfleet Long-Range Scout')
ships.append('Starfleet Fast Attack Ship')
ships.append('Klingon Assault Ship')
ships.append('Klingon Tactical Assault Ship')
ships.append('Klingon Hunter-Killer')
ships.append('Romulan Cutter')
ships.append('Romulan Light Fighter')
ships.append('Romulan Warpshuttle')

ships_labels = {}
ships_rev_labels = {}
for i in range(0, len(ships)):
    ships_labels[i] = ships[i]

for i in range(0, len(ships)):
    ships_rev_labels[ships[i]] = i

stats = {}

for i in range(0, len(ships)):
    ships_stats = []
    for j in range(0, TOTAL_STATS):
        v = uniform(0.0, 100.0)
        z = uniform(0.0, 100.0)*v
        x = round(random()*z, 2)
        y = round(x+random()*z, 2)
        ships_stats.append([x, y])
    stats[i] = ships_stats


print("=================================== StarFleet Intelligence Reports==============================================")
for i in range(0, len(ships)):
    for k in range(0, 100):
        rand_stat = []
        for j in range(0, TOTAL_STATS):
            rand_stat.append(round(uniform(stats[i][j][0], stats[i][j][1]), 2))
        print(rand_stat, ships_labels[i])

print("================================================================================================================")

for t in range(0, TOTAL_BATTLES):
    rand_ship = int(uniform(0, len(ships)))
    rand_name = ships[rand_ship]
    rand_stat = []
    for j in range(0, TOTAL_STATS):
        rand_stat.append(
            round(uniform(stats[rand_ship][j][0], stats[rand_ship][j][1]), 2))
    #print("Random: %s" % rand_name)
    print("A ship approaches: ", rand_stat)
    decision = input("Fire (Y/N) >")
    if decision == "Y" and "Starfleet" not in rand_name:
        print("Congrats! Stafleet confirms you destroyed a: %s" % rand_name)
    elif decision == "Y" and "Starfleet" in rand_name:
        print(
            "Report to Lya Station Alpha for court-martial. You destroyed a %s." % rand_name)
        exit(0)
    elif decision == "N" and "Starfleet" not in rand_name:
        print("A %s has destroyed your ship" % rand_name)
        exit(0)
    elif decision == "N" and "Starfleet" in rand_name:
        print("A %s has arrived to support you." % rand_name)
    else:
        print("You failed to make a decision.")
        exit(0)

print(
    "Congrats, the war is over: shctf{F3Ar-1s-t4E-true-eN3my.-Th3-0nly-en3my}")
