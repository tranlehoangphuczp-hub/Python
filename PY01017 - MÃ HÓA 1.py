from math import *
import array
def solve(s):
    a = []
    cnt = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            print(str(cnt) + s[i], end = '')
            cnt = 1
    print(str(cnt) + s[len(s)-1])
    print()
t = int(input())
while t > 0:
    n = input()
    solve(n)
    t -= 1