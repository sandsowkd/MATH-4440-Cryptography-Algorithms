import math
import random
import sympy
import numpy as np

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


def BDayAttack(g,h,p):
    N = math.ceil(math.sqrt(p-1)) 
    powers = {}
    for i in range(N):
        j = int(random.uniform(0,p))
        powers[pow(g,j,p)] = j
    inv = inverse(g, p)
    while (True):
        j = int(random.uniform(0,p))
        k = (h * pow(inv,j,p)) % p
        if k in powers:
            return (powers[k] + j) % (p - 1)


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


def generatefactorbase(n):
    bases = []
    for i in range(2, n+1):
        if sympy.isprime(i):
            bases.append(i)
    return bases


def factor(b,n):
    vec = [0] * len(b)
    num = n
    i = 0
    while (i < len(b)):
        if (num % b[i] == 0):
            num /= b[i]
            vec[i] += 1
        else:
            i += 1
    if (num == 1):
        return True, vec
    else:
        return False, vec


def isindependent(list, biglist):
    matr = np.array(biglist)
    biglist.append(list)
    matrr = np.array(biglist)
    rank = np.linalg.matrix_rank(matr)
    rankk = np.linalg.matrix_rank(matrr)
    if (rank + 1 == rankk):
        return True
    else:
        return False



def IndexCalculus(b,g,h,p):
    while (True):
        biglist = []
        indeplist = []
        dictionary = {}
        rank = 0
        while (rank < len(b)):
            k = int(random.uniform(1,p))
            works, factored = factor(b,pow(g,k,p))
            #print(isindependent(factored, biglist))
            if (works and (not factored in biglist) and isindependent(factored, biglist)):
                dictionary[tuple(factored)] = k
                biglist.append(factored)
                indeplist.append(factored)
                rank += 1
        matr = np.array(indeplist)
        matr = np.transpose(matr)
        det = np.linalg.det(matr)
        if (Euclidean(round(np.linalg.det(matr)), p-1) != 1):
            continue
        det = round(np.linalg.det(matr))
        invmatr = np.linalg.inv(matr)
        invmatr *= np.linalg.det(matr)
        invmatr = (np.rint(invmatr)).astype(int)
        detinv = inverse(det, p-1)
        invmatr *= detinv
        with np.nditer(invmatr, op_flags=['readwrite']) as it:
            for x in it:
                x[...] = x % (p-1)

        print("Random factorizations of g^x we use:",dictionary)
        while (True):
            k = int(random.uniform(0,p))
            works, factored = factor(b, (h * pow(g,k,p)) % p)
            if (not works):
                continue
            vec = np.array(factored)

            print("We see h*g^k with k =",k, "has factorization", vec)
            ansvec = invmatr.dot(vec)

            sum = 0
            for i in range(len(ansvec)):
                sum += ansvec[i]*(dictionary[tuple(indeplist[i])])
            return (sum-k) % (p-1)
        