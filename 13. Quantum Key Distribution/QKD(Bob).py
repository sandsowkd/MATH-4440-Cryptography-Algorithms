import math
import functions
import sympy
import random


n = []
for i in range(16):
    n.append(int(random.uniform(0,2)))
print(n)

Alicebases = functions.generateQKDbases(len(n))
Bobbases = functions.generateQKDbases(len(n))
print("Your bases: ", Alicebases)
print("Bob's bases:", Bobbases)

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