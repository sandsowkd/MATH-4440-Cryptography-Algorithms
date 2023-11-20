import math
import functions
import sympy
import random

n = input("Number to factor: ")
n = int(n)
if (sympy.isprime(n)):
    print(n, "is a prime")
    exit()

b = input("Generate (prime) factor base with largest number: ")
b = int(b)
bases = functions.generatefactorbase(b)

print("We will use the factoring base: ", bases)

#bases = [2,3,5,7,11,13]

print("We found the factor: ", functions.quadraticsieve(bases,n))