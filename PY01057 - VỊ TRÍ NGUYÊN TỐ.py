from math import *
a = [2, 3, 5, 7]
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def solve(s):
    for i in range(len(s)):
        if (isPrime(i) and ( int(s[i]) not in a )) or (not isPrime(i) and int(s[i]) in a):
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(solve(s))
        t -= 1