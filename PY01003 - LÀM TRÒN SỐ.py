def Roundd(n):
    z = str(n)
    s = ""
    while n > 10:
       du = n % 10
       n //= 10
       if du >= 5:
           n += 1
    s = str(n) + s
    if z[0:1] == '9' and z[1:2:] >= '5':
        print('1'+'0'*len(z))
        return
    if len(s) < len(z):
        s = s + ('0'*(len(z)-len(s)))
    print(s)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        Roundd(n)
        t -= 1