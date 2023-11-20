import math
import functions
import sympy
import random

#Alice's Setup:
p = input("First Prime: ")
p = int(p)
if (not sympy.isprime(p)):
    print("Not a prime")
    exit()

q = input("Second Prime: ")
q = int(q)
if (not sympy.isprime(q)):
    print("Not a prime")
    exit()

n = p * q
totient = (p - 1) * (q - 1)

e = int(random.uniform(0,n)) #Finding e relatively prime to totient
while (functions.Euclidean(e,totient) != 1):
    e = int(random.uniform(0,n))

d = functions.inverse(e, totient) #Inverse of e (that we will use later)

#Alice will send e and n to Bob

#message = int(random.uniform(0,n))
message = 100
print("The message Bob is trying to send is", message)

#Bob will send encoded message (message ^ e) to Alice
encoded = pow(message, e, n)

#Alice recieves this, decodes by taking encoded ^ d
decode = pow(encoded, d, n)

print("Alice decoded the message to: ", decode)
if (message == decode):
    print("Alice successfully decoded!")
else:
    print("Something went wrong")