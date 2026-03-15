import array
from math import *
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
t = int(input())
while t > 0:
    a = []
    n = int(input())
    for i in range(10, n):
        k,m = i, int(str(i)[::-1])
        if isPrime(k) and k != m and isPrime(m) and m <= n:
            if k not in a and m not in a:
                a.append(k)
                a.append(m)
                print(k,m,end = " ")
    print()
    t -= 1