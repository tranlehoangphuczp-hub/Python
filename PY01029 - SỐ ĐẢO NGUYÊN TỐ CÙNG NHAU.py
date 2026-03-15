from math import *
import array
def solve(n):
    num1 = n
    num2 = 0
    while num1 > 0:
        num2 = num2*10 + (num1%10)
        num1 //= 10
    if gcd(n, num2) == 1:
        print("YES")
    else:
        print("NO")
t = int(input())
while t > 0:
    z = int(input())
    solve(z)
    t -= 1