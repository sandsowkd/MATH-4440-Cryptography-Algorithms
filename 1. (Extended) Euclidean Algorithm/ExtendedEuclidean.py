import math
import functions

a = input("First number: ") #Inputs for Bezout Coefficients
a = int(a)
b = input("Second number: ")
b = int(b)

print("(",functions.ExtendedEuclidean(a,b)[0], "*", a,")", "+","(", functions.ExtendedEuclidean(a,b)[1], "*", b,")", "=",functions.Euclidean(a,b))
#print("The GCD of",a,'and',b,'is', Euclidean(a,b))

