import math
import functions

print("First number:") #Taking inputs
a = input()
a = int(a)
print("Second number:")
b = input()
b = int(b)

print("(",functions.ExtendedEuclidean(a,b)[0], "*", a,")", "+","(", functions.ExtendedEuclidean(a,b)[1], "*", b,")", "=",functions.Euclidean(a,b))
#print("The GCD of",a,'and',b,'is', Euclidean(a,b))

