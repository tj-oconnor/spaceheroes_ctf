from colorama import *
from sys import *


prophecy = "throUghoutourliVingnightMareaswebattlewIththiSunYieLDingdArKnesswechoZoseealightthislightglowsWithPrOmisEchasisgtheshadowsCastBytheGReaTpoisonandpuriFyiNgwhicHgrowntoXic"
string = "UI-KO TH-NV GE-LB KC-RN PD-DN"
count = 0
cutoff = '---------------------------'
temp = ''
print(cutoff)
for i in prophecy:
    if i.isupper():
        stdout.write(f'|{Fore.RED}{i}{Fore.WHITE}')
    else:
        stdout.write(f'|{i}')
    count += 1
    if count == 13:
        stdout.write(f'|\n')
        count = 0

print(cutoff)
print(string)
