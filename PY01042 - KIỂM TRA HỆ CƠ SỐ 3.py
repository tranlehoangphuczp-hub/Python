from math import *
import array
def solve(s):
    for i in s:
        if i != "1" and i != "2" and i != "0":
            return "NO"
    return "YES"
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(solve(s))
        t -= 1