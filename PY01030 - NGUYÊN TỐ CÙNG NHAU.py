from math import *
import array
n, m=map(int, input().split())
cnt = 0
for i in range((10 ** (m-1)), (10 ** m)):
    if cnt == 10:
        print()
        cnt = 0
    if gcd(n,i) == 1:
        cnt += 1
        print(i, end = ' ')