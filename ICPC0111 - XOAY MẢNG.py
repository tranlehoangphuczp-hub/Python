from math import *
import array
def solve(a, n, m):
    for i in range(m):
        a.append(a[i])
    for i in range(m, len(a)):
        print(a[i], end = ' ')
    print()
t = int(input())
while t > 0:
    n,m = map(int, input().split())
    a = []
    s = input().split()
    for i in range(n):
        a.append(int(s[i]))
    solve(a,n,m)
    t -= 1