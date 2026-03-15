x = input()
cnt = 0
for i in range(0,len(x)):
    if x[i] == "4" or x[i] == "7":
        cnt += 1
if cnt == 7 or cnt == 4:
    print("YES")
else:
    print("NO")