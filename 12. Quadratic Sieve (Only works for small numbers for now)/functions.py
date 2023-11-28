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


def squareroot(p,n):
    list = []
    if (p==2):
        list.append(n % 2)
    else:
        for i in range(0, p//2 + 1):
            if ((i**2) % p == n % p):
                list.append(i)
                list.append(p-i)
    if (0 in list):
        print("We have a factor:", p)
        exit()
    return list


def modifyfactorbase(b,n):
    for p in b:
        if ([] == squareroot(p,n)):
            b.remove(p)
    return b


def quadfactor(b,k,n): #b = factor base, k = index, n = number tryna factor
    a = k**2 - n #Number to go down to 0
    factor = [0]*len(b) #Factor vector
    for i in range(len(b)):
        if (k % b[i]) in squareroot(b[i], n):
            while (a % b[i] == 0):
                a /= b[i]
                factor[i] += 1
    if (a == 1):
        return True, factor
    return False, factor



def mod2independent(list, biglist):
    listt = [0]*len(list)
    for i in range(len(list)):
        listt[i] = list[i] % 2
    for i in range(len(biglist)):
        for j in range(len(biglist[0])):
            (biglist[i])[j] = (biglist[i])[j] % 2
    matr = np.array(biglist)
    biglist.append(listt)
    matrr = np.array(biglist)
    rank = np.linalg.matrix_rank(matr)
    rankk = np.linalg.matrix_rank(matrr)
    if (rank + 1 == rankk):
        return True
    else:
        return False


def getsolution(b,listt):
    list = [[0]*len(b)]*len(listt)
    matr = np.array(list)
    for i in range(len(listt)):
        for j in range(len(b)):
            matr[i,j] = (listt[i][j]) % 2

    matr = np.transpose(matr)
    matr = np.c_[ matr , np.zeros(len(b))] 
    matrix = sympy.Matrix(matr).rref()
    ansvec = [0]*len(listt)
    ansvec[len(listt)-1] = 1
    for i in range(len(listt) - 1):
        ansvec[i] = -1*(matrix[0][(len(listt) + 1) * i + len(listt) - 1])
    
    for i in range(len(ansvec)):
        ansvec[i] = (round(ansvec[i])) % 2

    return ansvec
    


def quadraticsieve(b,n):
    N = math.ceil(math.sqrt(n))
    k = N
    count = 0
    diff = []
    dictionary = {}
    factored = []
    indeplist = []
    biglist = []

    while True:
        success, vec = quadfactor(b, k, n)
        if success:
            dictionary[tuple(vec)] = k
            indeplist.append(vec)
            if (not mod2independent(vec, biglist)):
                print("HERERE")
                break
        k += 1
        count += 1
    
    totalvec = [0]*len(b)
    prod1 = 1
    prod2 = 1
    ansvec = getsolution(b,indeplist)
    for i in range(len(ansvec)):
        if (ansvec[i] == 1):
            prod1 *= dictionary[tuple(indeplist[i])]
            for j in range(len(totalvec)):
                totalvec[j] += (indeplist[i])[j]
    
    for i in range(len(totalvec)):
        totalvec[i] //= 2
    
    for i in range(len(totalvec)):
        prod2 *= (b[i])**(totalvec[i])
    
    print(totalvec)
    print(dictionary)
    print(len(dictionary), len(b))
    print(ansvec)
    prod1 %= n
    prod2 %= n

    print(prod1, prod2)
    
    return Euclidean(prod1 - prod2, n)


'''def qquadraticsieve(b,n):
    N = math.ceil(math.sqrt(n))
    m = 100 #Will change later
    count = 0
    diff = []
    dictionary = {}
    factored = []
    indeplist = []
    biglist = []
    for k in range(N, N+m):
        diff.append(k**2 - n)
        factored.append([0]*len(b))
    for i in range(len(b)):
        for a in squareroot(b[i], n):
            for k in range(N, N+m):
                if (k % b[i] == a):
                    while (diff[k-N] % b[i] == 0):
                        diff[k-N] /= b[i]
                        (factored[k-N])[i] += 1


    for i in range(len(diff)):
        diff[i] = int(diff[i])
        if (diff[i] == 1):
            if (mod2independent(factored[i], biglist)):
                dictionary[tuple(factored[i])] = i+N
                indeplist.append(factored[i])
            else:
                dictionary[tuple(factored[i])] = i+N
                indeplist.append(factored[i])
                break

    totalvec = [0]*len(b)
    prod1 = 1
    prod2 = 1
    ansvec = getsolution(b,indeplist)
    for i in range(len(ansvec)):
        if (ansvec[i] == 1):
            prod1 *= dictionary[tuple(indeplist[i])]
            for j in range(len(totalvec)):
                totalvec[j] += (indeplist[i])[j]
    
    for i in range(len(totalvec)):
        totalvec[i] //= 2
    
    for i in range(len(totalvec)):
        prod2 *= (b[i])**(totalvec[i])
    
    print(totalvec)
    print(dictionary)
    print(ansvec)
    prod1 %= n
    prod2 %= n

    print(prod1, prod2)
    
    return Euclidean(prod1 - prod2, n)'''