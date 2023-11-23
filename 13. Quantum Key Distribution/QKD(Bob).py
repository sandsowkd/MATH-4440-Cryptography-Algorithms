import math
import functions
import sympy
import random

#What Bob generates:
n = []
for i in range(16):
    n.append(int(random.uniform(0,2)))

Alicebases = functions.generateQKDbases(len(n))
Bobbases = functions.generateQKDbases(len(n))

#What you recieved:
recieved = []
for i in range(len(n)):
    if (Alicebases[i] == Bobbases[i]):
        recieved.append(n[i])
    else:
        recieved.append(int(random.uniform(0,2)))

print("You recieved this from Bob: ", recieved)
print("Alice's bases:", Alicebases)
print("Your bases:   ", Bobbases)


shared = []
for i in range(len(n)):
    if (Alicebases[i] == Bobbases[i]):
        shared.append(n[i])

g = input("What do you think the shared secret is: ")
g = [*g]
for i in range(len(g)):
    g[i] = int(g[i])

if (g == shared):
    print("Correct!")
else:
    print("Incorrect, the shared secret is: ", shared)