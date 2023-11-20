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
        
