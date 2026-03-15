from math import *
import array

P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
lst = list(P)
def solve(n, s):
    z = ""
    for i in range(len(s)):
        a = P.index(s[i])
        z += lst[(a + n) % 28]
    rever = z[::-1]
    print(rever)

if __name__ == "__main__":

    ok = True
    while ok:
        z = list(map(str, input().split()));
        if int(z[0]) == 0:
            break
        solve(int(z[0]), z[1])