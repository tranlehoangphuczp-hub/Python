from math import*
import array
def isPrime(s):
    sum = 0
    for c in s:
        sum += int(c)
    z = int(sqrt(sum))
    for i in range(2, z+1):
        if sum % i == 0:
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