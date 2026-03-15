def solve(s):
    for i in range(0, len(s), 2):
        print(s[i] * int(s[i+1]), end ='')
n = int(input())
for i in range(n):
    solve(input())
    print('')