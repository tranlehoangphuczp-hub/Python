from math import *
import array
def solve(s, x):
    cnt = 0
    cnt1 = len(s)
    cnt2 = len(x)
    result = 0;
    while cnt < cnt1:
        if s[cnt:cnt + cnt2:] == x:
            result += 1
            cnt += cnt2
        else:
            cnt += 1
    return result
if __name__=='__main__':
    t = int(input())
    while t > 0:
        s = input()
        x = input()
        print(solve(s, x))
        t -= 1