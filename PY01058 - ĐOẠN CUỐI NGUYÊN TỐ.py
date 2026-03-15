from math import *
import array
def isPrime(s):
    z = int(s[len(s)-4:len(s)])
    if z < 2:
        return False
    for i in range(2,int(sqrt(z))+1):
        if z % i == 0:
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        if isPrime(s):
            print("YES")
        else:
            print("NO")
        t -= 1
