j = int(input())
if j % 4 == 0 and j % 100 != 0 or j % 400 == 0:
    print(1)
else:
    print(0)