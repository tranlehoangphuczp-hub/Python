from math import *
import array
def solve(n):
    Sum = 0
    if n % 2 == 0:
        for i in range(2,n+1, 2):
            Sum += 1 / i
        print('%.6f' % Sum)
    elif n % 2 == 1:
        for i in range(1,n+1, 2):
            Sum += float(1) / float(i)
        print('%.6f' % Sum)
t = int(input())
while t > 0:
    z = int(input())
    solve(z)
    t -= 1