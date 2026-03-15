s = input()
res = s.lower()
z = res[len(s)-3::]
if z == ".py":
    print("yes")
else:
    print("no")