import math
import functions
import sympy
import random

p = input("Prime: ")
p = int(p)
if (not sympy.isprime(p)):
    print("Not a prime")
    exit()

g = input("Generator: ")
g = int(g)
if (not sympy.is_primitive_root(g, p)):
    print("Not a generator")
    exit()

aliceprivate = input("Your private key (will be taken mod p): ")
aliceprivate = int(aliceprivate) % p

alicepublic = pow(g, aliceprivate, p)

bobprivate = int(random.uniform(0,p))
bobpublic = pow(g, bobprivate, p)

sharedkey = pow(bobpublic, aliceprivate, p)

print("Your public key is", alicepublic, ", Bob's public key is", bobpublic, ", and the shared key is", sharedkey)
print("From your perspective, the shared key is (Bob's public)^(Your private) mod p: ", sharedkey, " = ", bobpublic, "^", aliceprivate, " Mod ", p, sep='')
print("From Bob's perspective, the shared key is (Your public)^(Bob's private) mod p: ", sharedkey, " = ", alicepublic, "^", bobprivate, " Mod ", p, sep='')