num = []
hol = []
for i in range (0, 7):
    n = int(input())
    num.append(n)
for i in range(0, 7):
    if num[i] % 2 == 1 :
        hol.append(num[i])
if len(hol) == 0 :
    print("-1")
else:
    print(sum(hol))
    print(min(hol))