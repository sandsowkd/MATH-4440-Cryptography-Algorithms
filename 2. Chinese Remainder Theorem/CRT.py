import math
import functions

n = input("List of Moduli: ").split()
for i in range(len(n)):
    n[i] = int(n[i])

for i in n:
    if i <= 0:
        print("Please give Positive integer Moduli")
        exit()

a = input("List of Remainders: ").split()
for i in range(len(a)):
    a[i] = int(a[i])

if (len(n) != len(a)):
    print("Error: Different number of Moduli and Remainders")
    exit()

for i in range(len(n)):
    for j in range(i+1,len(n)):
        if (functions.Euclidean(n[i],n[j]) != 1):
            print("Moduli are not pairwise relatively prime")
            exit()

for i in range(len(n)):
    a[i] = a[i] % n[i]

print("Combining these Congruences yield:", functions.CRT(a,n)[0], "Mod", functions.CRT(a,n)[1])

