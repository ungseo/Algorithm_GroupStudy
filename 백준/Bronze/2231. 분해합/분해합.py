n = int(input())
ans = []
flag = 0


for i in range(n, 0, -1):
    a = str(i)
    sum = 0
    for j in a:
        sum += int(j)
    if i + sum == n:
        flag = 1
        ans.append(i)
if flag == 0:
    print(0)
else:
    print(min(ans))