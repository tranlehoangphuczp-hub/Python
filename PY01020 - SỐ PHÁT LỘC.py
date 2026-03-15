def solve(s):
    if s[len(s)-2] == '8' and s[len(s)-1] == '6':
        return "YES"
    else:
        return "NO"
n = int(input())
while n > 0:
    print(solve(input()))
    n-=1