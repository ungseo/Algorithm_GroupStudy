lst = list(map(int, input().split()))

temp = []
flag = 1
for i in range(1, 7):
    if lst.count(i) == 0: continue
    if lst.count(i) == 3:
        print(10000 + i * 1000)
        flag = 0
    elif lst.count(i) == 2:
        print(1000 + i * 100)
        flag = 0
    else:
        temp.append(i)
if flag == 1:
    print(max(temp) * 100)
