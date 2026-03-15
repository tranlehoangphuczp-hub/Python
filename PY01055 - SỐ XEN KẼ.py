from math import *
def solve(s):
    if len(s) % 2 == 0:
        return "NO"
    for i in range(2,len(s)+1, 2):
        if s[i] != s[i-2]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(solve(s))
        t -= 1