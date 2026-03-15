def Sum(num):
    sum = 0
    while num >= 1:
        sum += num % 10
        num //= 10
    if sum % 10 == 0:
        return True
    return False
def solve(num):
    for i in range(len(num)):
        if abs(ord(num[i])-ord(num[i+1])) != 2:
            return False
        return True
n = int(input())
while n > 0:
    z = int(input())
    if Sum(z) and solve(str(z)):
        print("YES")
    else:
        print("NO")
    print('')
    n -= 1