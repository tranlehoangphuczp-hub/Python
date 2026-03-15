def Try(s,n,a,b,c):
    lst = []
    if len(s) == n and a > 0 and a <= b and b <= c:
        lst.append(s)
    elif len(s) < n:
        Try(s + 'A',n,a+1,b,c)
        Try(s + 'B',n,a,b+1,c)
        Try(s + 'C',n,a,b,c+1)
    lst.sort()
    for i in lst:
        print(i)

if __name__ == '__main__':
    n = int(input())
    for i in range(3, n+1):
        Try("",i,0,0,0)