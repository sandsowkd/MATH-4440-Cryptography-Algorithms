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


#What Alice Does: (sends alicepublic to Bob, along with g, p)
aliceprivate = input("Your private key (will be taken mod p): ")
aliceprivate = int(aliceprivate) % p

alicepublic = pow(g, aliceprivate, p)

#Bob's Ephemeral key
bobprivate = int(random.uniform(0,p))
bobpublic = pow(g, bobprivate, p)

#message = int(random.uniform(0,p))
message = 100
print("The message Bob is trying to send is", message)
Bobsharedkey = pow(alicepublic, bobprivate, p)

#Bob will send bobpublic, encoded message (message*shared) to Alice
encoded = (message * Bobsharedkey) % p

#Alice recieves this, calculates shared key inverse, multiplies onto encoded
Alicesharedkey = pow(bobpublic, aliceprivate, p)
inv = functions.inverse(Alicesharedkey, p)
decode = (encoded * inv) % p

print("Your public key is", alicepublic, ", Bob's public key is", bobpublic)
print("The encoded message Bob sends is", encoded, ", which Alice decodes as", decode)
if (message == decode):
    print("Alice successfully decoded!")
else:
    print("Something went wrong")