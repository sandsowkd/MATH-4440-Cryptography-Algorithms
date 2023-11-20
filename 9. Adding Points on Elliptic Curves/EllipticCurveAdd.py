import math
import functions
import sympy
import random

p = input("Give the size of the Finite field (prime or 0 if none): ")
p = int(p)
if (p < 0):
    print("Please give a prime or 0")
    exit()
if (not (sympy.isprime(p) or p == 0)):
    print("Please give a prime or 0")
    exit()


c = input("Elliptic Curve Coefficients (a and b in y^2 = x^3 + ax + b): ").split()
if (len(c) != 2):
    print("Please give 2 Integer Coefficients")
    exit()
for i in range(2):
    c[i] = int(c[i])

if (p == 0):
    a = c[0]
    b = c[1]
else:
    a = c[0] % p
    b = c[1] % p

if (p == 0):
    if (4 * (a**3) + 27 * (b**2) == 0):
        print("The Elliptic Curve is singular. Try again")
        exit()
else:
    if ((4 * (a**3) + 27 * (b**2)) % p == 0):
        print("The Elliptic Curve is singular. Try again")
        exit()



x = input("First point Coordinates (use (0,0) for infinity): ").split()
if (len(x) != 2):
    print("Please give 2 Values")
    exit()
for i in range(2):
    x[i] = int(x[i])

if (x[0] != 0 or x[1] != 0):
    if (p == 0):
        functions.testregcurve(a,b,x[0],x[1])
    else:
        x[0] = x[0] % p
        x[1] = x[1] % p
        functions.testffcurve(p,a,b,x[0],x[1])



y = input("Second point Coordinates (use (0,0) for infinity): ").split()
if (len(y) != 2):
    print("Please give 2 Values")
    exit()
for i in range(2):
    y[i] = int(y[i])

if (y[0] != 0 or y[1] != 0):
    if (p == 0):
        functions.testregcurve(a,b,y[0],y[1])
    else:
        y[0] = y[0] % p
        y[1] = y[1] % p
        functions.testffcurve(p,a,b,y[0],y[1])



if (p == 0):   
    x3,y3 = functions.addregcurve(a,b,x[0],x[1],y[0],y[1])
else:
    x3,y3 = functions.addffcurve(p,a,b,x[0],x[1],y[0],y[1])

if (x3 == 0 and y3 == 0):
    print("We get the point Infinity: (0,0)")
else:
    print("We get the point: (", x3,',',y3,')', sep = '')