def solve(s):
    s1 = []
    s2 = []
    for c in s:
        s1.append(c)
    for i in list(reversed(s1)):
        s2.append(i)
    for i in range(1,len(s1)):
        if abs((ord(s1[i]) - ord(s1[i - 1]))) != abs((ord(s2[i]) - ord(s2[i - 1]))):
            return "NO"
    return "YES"

n = int(input())
while n > 0:
    s = str(input())
    print(solve(s))
    print('')
    n -= 1