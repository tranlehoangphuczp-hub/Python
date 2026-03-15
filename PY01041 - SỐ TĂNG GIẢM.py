from math import *
import array
def solve(s):
    if len(s) < 3:
        return "NO"
    a = list(s)
    cnt = 0
    for i in range(len(a)-2):
        if a[i] == a[i+1] or (a[i] > a[i+1] and a[i+1]  < a[i+2]):
            return "NO"
    return "YES"
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(solve(s))
        t -= 1