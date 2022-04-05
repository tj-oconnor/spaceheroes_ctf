import dis
import math


def chalfn():  # Challenge function
    a = input("Enter the super secret password:")
    b = ""
    c = 0
    for x in a:  # Swaps out a few letters
        if x == 'a':
            b += '@'
        if x == '@':
            b += 'a'
        elif x == 'o':
            b += '0'
        elif x == '0':
            b += 'o'
        elif x == 'e':
            b += '3'
        elif x == '3':
            b += 'e'
        elif x == 'l':
            pass
        else:
            b += x
        c += 1

    d = "S0th3combination1sonetw0thr3efourf1ve"
    if (c % 4 == 0):  # Length needs to be multiple of 4
        if b == d:
            print("You got the flag!")
            exit()

    print("Oops, try again.")


chalfn()
dis.dis(chalfn)  # Disassemble the function
