def check(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return "NO"
    return "YES"
n = int(input())
for i in range(n):
    z = input()
    print(check(z))