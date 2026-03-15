from math import *
def solve(s):
    res = 1
    for i in s:
        if int(i) != 0:
            res *= int(i)
    return res

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(solve(s))
        t -= 1