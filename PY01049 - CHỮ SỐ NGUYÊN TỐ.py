from math import*
import array
def isPrime(n):
    if n < 2:
        return False
    elif n >= 2:
        z = int(sqrt(n));
        for i in range(2, z+1):
            if n % i == 0:
                return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        num1 = 0
        num2 = 0
        for c in s:
            if isPrime(int(c)):
                num1 += 1
            else:
                num2 += 1
        if isPrime(len(s)) and num1 > num2:
            print("YES")
        else:
            print("NO")
        t -= 1