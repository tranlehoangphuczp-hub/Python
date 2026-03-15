import array
from math import *
def check(s):
    if s[0] != s[len(s)-1]:
        return False
    return True
t = int(input())
while t > 0:
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
    t -= 1