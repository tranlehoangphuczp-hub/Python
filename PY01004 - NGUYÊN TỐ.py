from math import *
def CheckNT(a):
    if a < 2:
        return False
    else:
        for i in range(2, int(sqrt(a)+1)):
            if a % i == 0:
                return False
        return True

n  =int(input())
while n > 0:
    z = int(input())
    cnt = 0
    for i in range(1, z):
        if gcd(i, z) == 1:
            cnt += 1