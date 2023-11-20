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


def testffcurve(n,a,b,p0,p1):
    if ((p1**2 % n) != ((p0**3 + a * p0 + b) % n)):
        print("Point is not on Elliptic Curve")
        exit()
    return


def addffcurve(n,a,b,x0,x1,y0,y1):
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

        if (Euclidean(2 * x1, n) != 1):
            print("Error adding points: no inverse of: ", (2 * x1) % n)
            return -1, Euclidean(2 * x1, n)
        slope = ((3*(x0**2) + a) * inverse(2 * x1, n)) % n
        intercept = (x1 - x0 * slope) % n
        xthird = (slope**2 - x0 - x0) % n
        ythird = (slope*xthird + intercept) % n
        yans = -ythird % n
        return xthird, yans

    if (Euclidean(y0 - x0, n) != 1):
            print("Error adding points: no inverse of: ", (y0 - x0) % n)
            return -1, Euclidean(y0 - x0, n)
    slope = ((y1 - x1) * inverse( y0 - x0 , n)) % n
    intercept = (x1 - x0 * slope) % n
    xthird = (slope**2 - x0 - y0) % n
    ythird = (slope*xthird + intercept) % n
    yans = -ythird % n
    return xthird, yans


def EllipticCurveFactoring(n,a,b,x0,x1):
    num = 1
    x = x0
    y = x1
    xx = x
    yy = y
    while(True):
        print("Here",x,y,num)
        for i in range(num):
            xx,yy = addffcurve(n,a,b,x,y,xx,yy)
            #print(xx,yy)
            if (xx == -1):
                print("We have the factor: ", yy)
                exit()
        num += 1
        x = xx
        y = yy
