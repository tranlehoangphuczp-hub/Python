n = int(input())
while n > 0:
    s = input()
    if s[0:2] == s[len(s)-2:len(s)]:
        print("YES")
    else:
        print("NO")
    n -= 1
