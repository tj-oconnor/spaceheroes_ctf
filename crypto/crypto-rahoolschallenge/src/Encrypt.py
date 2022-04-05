# Not a very pretty encryptor but it works, decrypts as you go for proof checking
import string

aaa = ""
bbb = ""
rev = ""
ccc = ""
counter = 0
while(1):
    x = input("enter x")
    if (x == "9"):# Exits loop
        break
    elif (x == "8"):# Makes a Space
        aaa = aaa+" "
        rev = rev+" "
        bbb = bbb+" "
        ccc = ccc+" "
    else:
        xx = ord(x)-97# Converts from ASCII to positional
        if counter == 0:# Keeps track of what key letter to use
            yy = ord('E')
            ccc = ccc + 'E'
        elif counter == 1:
            yy = ord('X')
            ccc = ccc + 'X'
        elif counter == 2:
            yy = ord('O')
            ccc = ccc + 'O'
        elif counter == 3:
            yy = ord('T')
            ccc = ccc + 'T'
        elif counter == 4:
            yy = ord('I')
            ccc = ccc + 'I'
        elif counter == 5:
            yy = ord('C')
            ccc = ccc + 'C'
        
        counter = (counter + 1) % 6# Ensures counter loops
    
        z = (xx+yy)%26# Converts by adding positional of message letter with ASCII decimal of key letter
        aaa = aaa+str(z)# Keeps track of number for that index
        rev = rev + chr(((z-yy)%26)+97)# Keeps track of a reversed letter ie the message letter for index for checking
        bbb = bbb + chr(z+97)# The actual string of encrypted letters
        
print(aaa)
print(rev)
print(ccc)# Self checking that EXOTIC repeats
print(bbb)

# nice job decrypting input the answer as the key with the e as a three the o as a zero with the word engram after with the a as a four and aognebr right after
