from math import *
import array
def solve(s):
    z = s[::-1]
    a = []
    for i in range(len(s)-1):
        a.append(abs(ord(s[i])-ord(s[i+1])))
    for i in range(len(z)-1):
        if abs(ord(z[i])-ord(z[i+1])) != a[i]:
            return "NO"
    return "YES"

if __name__=='__main__':
    t = int(input())
    while t > 0:
        s = input()
        print(solve(s))
        t -= 1