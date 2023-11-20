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

print("We get the exponent: ",functions.BSGSDLP(g,h,p), sep = '')