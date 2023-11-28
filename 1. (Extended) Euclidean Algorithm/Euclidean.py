import math
import functions

a = input("First number: ") #Inputs for GCD
a = int(a)
b = input("Second number:")
b = int(b)

print("The GCD of",a,'and',b,'is', functions.Euclidean(a,b))
