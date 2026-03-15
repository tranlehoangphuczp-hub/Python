a, K, N = map(int, input().split())
z = N // K
ok = False
for i in range(1, z + 1):
    b = (K*i)-a
    if b > 0 and a + b <= N:
        print(b,end = " ")
        ok = True
if not ok:
    print(-1)