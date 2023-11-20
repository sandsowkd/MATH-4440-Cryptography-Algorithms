import math
import functions
import sympy
import random

n = input("Number to factor: ")
n = int(n)
if (sympy.isprime(n)):
    print(n, "is a prime")
    exit()
if (n <= 1):
    print("Please enter a positive integer larger than 1")
    exit()


c = input("Elliptic Curve Coefficients (a and b in y^2 = x^3 + ax + b): ").split()
if (len(c) != 2):
    print("Please give 2 Integer Coefficients")
    exit()
for i in range(2):
    c[i] = int(c[i])

a = c[0] % n
b = c[1] % n

if ((4 * (a**3) + 27 * (b**2)) % n == 0):
    print("The Elliptic Curve is singular. Try again")
    exit()



x = input("First point Coordinates: ").split()
if (len(x) != 2):
    print("Please give 2 Values")
    exit()
for i in range(2):
    x[i] = int(x[i])

x[0] = x[0] % n
x[1] = x[1] % n
functions.testffcurve(n,a,b,x[0],x[1])

print("Here")
print("We found the factor: ", functions.EllipticCurveFactoring(n,a,b,x[0],x[1]))
