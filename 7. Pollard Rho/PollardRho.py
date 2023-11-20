import math
import functions
import sympy
import random

n = input("Number to factor: ")
n = int(n)
if (sympy.isprime(n)):
    print(n, "is a prime")
    exit()

seed = input("Give a random seed to start with (default is 1): ")
try:
    seed = int(seed) & n
except ValueError:
    seed = 1

print(functions.PollardRho(seed, n))

