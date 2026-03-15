from math import *
import array
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, ceil(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
if __name__=='__main__':
    t = int(input())
    while t > 0:
        s = input()
        num1 = int(s[:3:])
        num2 = int(s[len(s)-3::])
        if isPrime(num1) and isPrime(num2):
            print("YES")
        else:
            print("NO")
        t -= 1