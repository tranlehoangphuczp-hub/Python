import math
def check(a):
    if a < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(a))+1):
            if a % i == 0:
                return False
        return True
def gcd(a,b):
    while b != 0:
        x = a % b
        a = b
        b = x
    return a
def Sum(a):
    cnt = 0
    while a >= 1:
        cnt += a % 10
        a = a // 10
    return cnt
for t in range(int(input())):
    a,b = [int(i) for i in input().split()]
    if check(Sum(gcd(a,b))):
        print("YES")
    else:
        print("NO")