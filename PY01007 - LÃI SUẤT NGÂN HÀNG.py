from math import *
import array
def solve(lst):
    cnt = 1
    while lst[0]*(1.0+lst[1]*0.01)**cnt < lst[2]:
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        lst = list(map(float , input().split()))
        solve(lst)
        t -= 1