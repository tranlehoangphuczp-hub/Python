from math import *
import array
def check(s):
    for i in range(len(s)-2):
        if s[i] != s[i+2]:
            return "NO"
    return "YES"
t = int(input())
while t > 0:
    print(check(input()))
    t -= 1
