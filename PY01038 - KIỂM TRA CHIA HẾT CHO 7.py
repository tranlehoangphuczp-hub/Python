from math import *
import array
def solve(n):
    cnt = 0
    sum = n
    while cnt <= 1000:
        cnt += 1
        sum += int(str(sum)[::-1])
        if sum % 7 == 0:
            print(sum)
            break
    if sum % 7 != 0:
        print(-1)

if __name__ == "__main__":
    t = int(input())
    while t > 0:
         n = int(input())
         if n % 7 == 0:
             print(n)
         else:
             solve(n)
         t -= 1