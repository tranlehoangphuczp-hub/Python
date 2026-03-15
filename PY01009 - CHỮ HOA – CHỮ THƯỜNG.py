s = input()
def check(s):
    num1 = 0;
    num2 = 0;
    for i in range(len(s)):
        if s[i] >= "A" and s[i] <= "Z":
            num1 += 1
        else:
            num2 += 1
    if num1 > num2:
        return True
    else:
        return False
if check(s)==True:
    print(s.upper())
else:
    print(s.lower())