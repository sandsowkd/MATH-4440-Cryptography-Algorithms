import math
import functions

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
    return functions.EuclideanHelper(a,b)


print("First number:") 
a = input()
a = int(a)
print("Second number:")
b = input()
b = int(b)

print("The GCD of",a,'and',b,'is', Euclidean(a,b))
