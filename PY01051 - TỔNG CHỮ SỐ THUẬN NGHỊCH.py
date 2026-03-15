from math import*
import array
def solve(s):
    sum = 0
    for c in s:
        sum += int(c)
    Sum = str(sum)
    if len(Sum) <= 1 or Sum != Sum[::-1]:
        return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        if solve(s):
            print("YES")
        else:
            print("NO")
        t -= 1