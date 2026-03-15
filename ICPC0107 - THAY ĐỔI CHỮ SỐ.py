from math import *
import array
t = int(input())
while(t > 0):
    num1, num2 = map(int, input().split())
    ip = input().split()
    if len(ip) == 1:
        s1 = ip[0]
        s2 = input()
    else:
        s1, s2 = ip
    if num1 > num2:
        num1,num2 = num2, num1
    s1 = s1.replace(str(num2), str(num1))
    s2 = s2.replace(str(num2),str(num1))
    print(int(s1) + int(s2), end=' ')
    s1 = s1.replace(str(num1), str(num2))
    s2 = s2.replace(str(num1), str(num2))
    print(int(s1) + int(s2))
    t -= 1