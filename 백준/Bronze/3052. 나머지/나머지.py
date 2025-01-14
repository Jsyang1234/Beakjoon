l = []
res = []
for i in range(1,11):
    n = int(input())
    l.append(n % 42)
for i in l :
    if i not in res :
        res.append(i)
print(len(res))
