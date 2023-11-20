import math
import functions

n = input("Number you want to test: ")
n = int(n)

a = input("List of Bases to test (should be primes smaller than number testing): ").split()
for i in range(len(a)):
    a[i] = int(a[i])

functions.MillerRabin(a,n)
