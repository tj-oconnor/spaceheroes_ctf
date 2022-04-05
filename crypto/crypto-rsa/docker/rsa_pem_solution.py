#
# Challenge inspiritation and process: https://blog.cryptohack.org/twitter-secrets
#

from Crypto.PublicKey import RSA
from Crypto.Util.number import isPrime

# Gather information from known values
#####################################################################
N_upper_bits = 0xca22da044dd64ff4e6bb7a0a203fbe95b2211043590f6f917c7badc394baa1d4f0d742d8b8724b180b36863165837d489cdaf35a303c98ad7568a4ec5ad1ba39d394f8d8a7eef52cf75f1e71ad9a233a138e72fc4f9a219331efcd83a7d41459e8821e4df82600dea5dc7b223311f800354fa57c680ad249035f2a842046bfe29c0e8b3b4aa2ff10683b5129b3c521060c513cbc5b89619644672802df2e178437abc2d52b58325b10e2a9d95c9e5da3f6cbf8e4026deb1b982911de0758886c0ab365ed9923f540a3fc15ff0e06e11189124cf283959e995c83e8903ef516cba897f61b42c2d3053aa8a3b7ea4bd3db5810ce3043207d18ec39856cdabdfb03586c1f0f1db33e8ad6fa20b3eccec3f2e2fa3859
p_lower_bits = 0x1836063cd965c8e0083995
q = 0xd36f2093bd46887ea77f84d39fcbb782ad47b1b13bca08aec96afe3ddd66176931b5b5128989bf8e60ae30b985d93b7b8936bd92969d0b00d12d61287c28925348b1b1447f3541b4b6b35449cf175fc20c5b82a0fd47a59f602a73e1af46246889cfc950dac7c6f8d4674797f0fd814874c57afc936525575d0ab7970df48ad522b6f50a65b4219c8928499046322943fd1a0a7ed8830fbc49e96e5468a1c0eec10f81af8ea88e788fee0e8b042e576e8c04c4299896b547815dc04f7c80d6350d24001e08d52151e2090b1f40776d0826186ffb66431e00ea1e3a1d919f7d2c1826c5f4a3dcc6c697d0f44e865739c2056cee9a5c4a3a7db3a3233cde2a747d
dp = 0x2868fb4c6db80589ebeabf499ea0d03c9d6cbf84dc9188b21cf78def9daac3782b2c03b4a504180137bd5bf778c88fb48c267c9b73976006c94a490ef5bc07c6c1459a99a15cf028d44989c120fac79ac8576cfe91485138b7bba81bc26deb03c63e3b1dbe29da338fd321cf452d81700d60275f0ee7a81ed713aa556fc862b1ca686d4c378fc58de6a294cbbb16f01d70017a9c2403e6b232348d7f03928efae471430b5403979a871db55c8426fd2df5565306ccce1a796fa1bb2780006f2ad2e07bda14aeb3d182d0f50af0afebd3a11e4367d87a5b581214733fb96b1f20144cee318a8a463c596a5db0ffde8948b4c0c8d2d7e3f97f9c2a7520eec4cce5
dq_upper_bits = 0xbf81882048eff9f1be04e26a4bf258e523ce2c443bc362d9edd5db326db66abdfd287839b219f2

# Identify possible p values
#####################################################################
e = 65537

for kp in range(3, e):
    p_mul = dp * e - 1
    if p_mul % kp == 0:
        p = (p_mul // kp) + 1
        if isPrime(p):
            print(f"Possible p: {p}")
            break

# Assert p is correct
##################################################################
p = 30895844709832899998188841662114790872234897752075001559021183621717400209605388312190323973252048528142263814004702009358055015498866420903698842271575438460613931365621046886345192942145776374845101190423906589600769824367560185523931386077331350130362227750110234305490531144015917135896267208021412360721347146788071177613105182982114511929718965668171007034208696471150694817629400494640735174627488595579043455808387304675315059251799971093060133716768702766322223249608212298602736927787573909617686015355115017336125464656230686512304637695993232618020104612242133267475115030618272782151467034194147619125653
N = p*q

assert hex(N).startswith(hex(N_upper_bits))

phi = (p-1)*(q-1)
d = pow(e, -1, phi)

# We have found the two prime factors of the modulus
assert isPrime(p) and isPrime(q) and p*q == N

# Our private exponent matches that from dp recovered
assert d % (p-1) == dp

# The top bits of the Modulus match those recovered
assert hex(N).startswith(hex(N_upper_bits))

# The prime p matches the low bits
assert hex(p).endswith(hex(p_lower_bits)[2:])

# The derived dq matches the recovered upper bits of dq
assert hex(d % (q-1)).startswith(hex(dq_upper_bits))

# Reconstruct RSA key and save it to a file
#####################################################

out = open("solved.pem", "w")
key = RSA.construct((N, e, d, p, q))
pem = key.export_key('PEM')
print(pem.decode())
out.write(pem.decode())
out.close()

# Make sure to use "chmod 700 solved.pem" to set accepted access permisions for ssh use
