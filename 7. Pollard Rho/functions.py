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
    