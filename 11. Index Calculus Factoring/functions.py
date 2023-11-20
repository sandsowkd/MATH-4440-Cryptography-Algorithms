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


def BSGSDLP(g,h,p):
    N = math.ceil(math.sqrt(p-1)) 

    powers = {}
    for i in range(N):
        powers[pow(g, i, p)] = i

    inv = inverse(g, p)
    bigG = pow(inv, N, p)


    for i in range(N):
        k = ((h * pow(bigG, i, p)) % p)
        if k in powers:
            return (i * N + powers[k]) % (p-1)

    return None


def PollardFunction(x, n):
    return (x**2 + 1) % n

def PollardRho(x0, n):
    list = [x0]
    i = 1
    while (True):
        for j in range(2):
            list.append(PollardFunction(list[len(list) - 1], n))
        gcd = Euclidean(list[i]-list[2*i], n)
        i += 1
        if (gcd == 1):
            continue
        elif (gcd == n):
            print("Failed to factor, try again.")
            exit()
        else:
            print("We found the factor: ", gcd)
            exit()


def testffcurve(p,a,b,p0,p1):
    if ((p1**2 % p) != ((p0**3 + a * p0 + b) % p)):
        print("Point is not on Elliptic Curve")
        exit()
    return


def testregcurve(a,b,p0,p1):
    if (p1**2 != (p0**3 + a * p0 + b)):
        print("Point is not on Elliptic Curve")
        exit()
    return


def addffcurve(p,a,b,x0,x1,y0,y1):
    if (x0 == 0 and x1 == 0 and y0 == 0 and y1 == 0):
        return 0,0
    elif (x0 == 0 and x1 == 0):
        return y0,y1
    elif (y0 == 0 and y1 == 0):
        return x0,x1
    elif (x0 == y0 and x1 != y1):
        return 0,0
    elif (x0 == y0 and x1 == y1):
        if (x1 == 0):
            return 0,0

        slope = ((3*(x0**2) + a) * inverse(2 * x1, p)) % p
        intercept = (x1 - x0 * slope) % p
        xthird = (slope**2 - x0 - x0) % p
        ythird = (slope*xthird + intercept) % p
        yans = -ythird % p
        return xthird, yans

    slope = ((y1 - x1) * inverse( y0 - x0 , p)) % p
    intercept = (x1 - x0 * slope) % p
    xthird = (slope**2 - x0 - y0) % p
    ythird = (slope*xthird + intercept) % p
    yans = -ythird % p
    return xthird, yans


def addregcurve(a,b,x0,x1,y0,y1):
    if (x0 == 0 and x1 == 0 and y0 == 0 and y1 == 0):
        return 0,0
    elif (x0 == 0 and x1 == 0):
        return y0,y1
    elif (y0 == 0 and y1 == 0):
        return x0,x1
    elif (x0 == y0 and x1 != y1):
        return 0,0
    elif (x0 == y0 and x1 == y1):
        if (x1 == 0):
            return 0,0

        slope = ((3*(x0**2) + a) / (2*x1))
        intercept = (x1 - x0 * slope)
        xthird = (slope**2 - x0 - x0)
        ythird = (slope*xthird + intercept)
        yans = -ythird
        return xthird, yans

    slope = ((y1 - x1)/(y0-x0))
    intercept = (x1 - x0 * slope)
    xthird = (slope**2 - x0 - y0)
    ythird = (slope*xthird + intercept)
    yans = -ythird
    return xthird, yans