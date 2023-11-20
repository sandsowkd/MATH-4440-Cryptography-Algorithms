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

h = input("The Discrete Log input (will be taken mod p): ")
h = int(h) % p

n = input("Generate (prime) factor base with largest number: ")
n = int(n)
bases = functions.generatefactorbase(n)

print("We will use the factoring base: ", bases)

#bases = [2,3,5,7,11]

print("We get the exponent: ",functions.IndexCalculus(bases,g,h,p), sep = '')