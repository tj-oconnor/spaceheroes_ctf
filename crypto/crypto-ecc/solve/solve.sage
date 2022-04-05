# Define elliptic curve
p = 11648516937377897327
a = 3820149076078175358
b = 1296618846080155687
E = EllipticCurve(GF(p), [0,0,0,a,b])

# Set Generator and Public Key
G = E([4612592634107804164, 6359529245154327104])
PubKey = E([9140537108692473465, 10130615023776320406])

# (x1,y1) is equal to k*G, where k is random
P1 = E([7657281011886994152, 10408646581210897023])
# Ciphertext is equal to M+(x2,y2), where (x2,y2) is equal to k*PubKey
C = E([5414448462522866853, 5822639685215517063])

# Initialize X to our generator 
X = G

# Public key is n*G, where n == PrivateKey
# If private key is small, we can brute force
for i in range(1, p):
     if X == PubKey:
         PrivKey = i
         print("[+] PrivateKey:", i)
         break
     # Point addition
     else:
         X = X + G

# Decryption is C - (n*P1)
Message = C - (PrivKey*P1)
print(Message)
