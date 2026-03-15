from math import *
import array

def solve(z):
    a = []
    n = ceil(sqrt(z))
    for i in range(2, n+1):
        while z % i == 0:
            a.append(i)
            z //= i
    if z != 1:
        a.append(z)
    b = []
    print(1, end='')
    for i in a:
        if i not in b:
            b.append(i)
            print(" *", str(i) + "^" + str(a.count(i)), end='')
    print()
t = int(input())
while t > 0:
    n = int(input())
    solve(n)
    t -= 1