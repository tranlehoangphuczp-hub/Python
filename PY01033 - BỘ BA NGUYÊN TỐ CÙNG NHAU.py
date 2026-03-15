from math import *
import array

a = []
z = list(map(int, input().split()))
for i in range(z[0], z[1]-1):
    for j in range(i+1,z[1]):
        for k in range(j+1, z[1]+1):
            if gcd(i,j) == 1 and gcd(j,k) == 1 and gcd(i,k) == 1:
                print("(" + str(i) + ", " + str(j) + ", " + str(k) + ")")