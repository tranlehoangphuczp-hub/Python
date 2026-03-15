import array
from math import *
def solve(i):
    if len(i) % 2 == 1 or i != i[::-1]:
        return False
    for j in i:
        if int(j) % 2 == 1:
            return False
    return True
t = int(input())
while t > 0:
    n = int(input())
    for i in range(22, n, 2):
        if solve(str(i)):
            print(i, end = " ")
    print()
    t -= 1