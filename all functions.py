import math
import random
import sympy

def EuclideanHelper(a, b):
    if (b == 0):
        return a
    return EuclideanHelper(b, a % b)

def Euclidean(a,b):
    if (a == 0 and b == 0): #Checking if (0,0)
        print("The GCD of (0,0) is undefined")
        exit()

    if (a < 0): #Changing negatives to positives (making life easier)
        a = -a
    if (b < 0):
        b = -b

    if (a < b): #Making b <= a to make recursion work better
        temp = a
        a = b
        b = temp
    return EuclideanHelper(a,b)


def ExtEuclideanHelper(a,b,c,d,e,f):
    if (b == 0):
        return a, b, c, d, e, f
    div = a // b
    return ExtEuclideanHelper(b, a % b, e, f, c - (div * e), d - (div * f))

def ExtendedEuclidean(a,b):
    if (a == 0 and b == 0): #Checking if (0,0)
        print("The GCD of (0,0) is undefined")
        exit()
    
    aneg = False
    bneg = False
    switch = False

    if (a < 0): #Changing negatives to positives (making life easier)
        a = -a
        aneg = True
    if (b < 0):
        b = -b
        bneg = True

    if (a < b): #Making b < a to make recursion work better
        temp = a
        a = b
        b = temp
        switch = True

    r1, r2, r3, r4, r5, r6 = ExtEuclideanHelper(a,b,1,0,0,1)

    if (switch):
        temp = r3
        r3 = r4
        r4 = temp
    if (aneg):
        r3 = -r3
    if (bneg):
        r4 = -r4

    return r3,r4


def inverse(a,n):
    if (Euclidean(a,n) != 1):
        print("No inverse exists")
        exit()
    return (ExtendedEuclidean(a % n, n)[0] % n)

def CRT(a,n):
    sum = 0
    product = 1
    for i in n:
        product *= i
    for i in range(len(n)):
        k = product/n[i]
        inv = inverse(k, n[i])
        sum += a[i] * k * inv
    return (int)(sum % product), product


def MillerRabin(bases,n):
    k = 0
    m = n-1
    while (m % 2 == 0):
        k += 1
        m /= 2
    m = int(m)
    for a in bases:
        prev = pow(a, m, n)
        for e in range(1,k+1):
            num = pow(a,m * pow(2,e), n)
            if (num == 1 and (prev != 1 and prev != n-1)):
                print(n, "is not a prime")
                return
            prev = num
        if (prev != 1):
            print(n, "is not a prime")
            return
    print(n, "is probably a prime")