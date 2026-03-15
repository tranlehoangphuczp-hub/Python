from math import *
import array
n = int(input())
def solve(s):
    a = []
    z = 0
    for i in range(len(s)):
        if s[i].isdigit():
            z = z * 10 + int(s[i])
        elif s[i].isalpha():
            if z != 0:
                a.append(z)
            z = 0
    a.append(z)
    a.sort()
    print(a[len(a)-1])
while n > 0:
    s = input()
    solve(s)
    n -= 1
