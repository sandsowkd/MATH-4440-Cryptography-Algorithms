import math
import functions

print("First number:") 
a = input()
a = int(a)
print("Second number:")
b = input()
b = int(b)

print("The GCD of",a,'and',b,'is', functions.Euclidean(a,b))
