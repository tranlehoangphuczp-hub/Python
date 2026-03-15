from math import *
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def solve(s):
    sum = 0
    for i in range(len(s)):
        if (i % 2 == 0 and int(s[i]) % 2 != 0) or (i % 2 == 1 and int(s[i]) % 2 == 0):
            return "NO"
        sum += int(s[i])
    if not isPrime(sum):
        return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(solve(s))
        t -= 1