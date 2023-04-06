import sys

input = sys.stdin.readline

dic = {}
lst = []
n = int(input())
sum = 0
for i in range(n):
    a = int(input())
    lst.append(a)
    sum += a
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

rst1 = round(sum / n)
rst2 = sorted(lst)[n // 2]
rst3 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
if len(rst3) != 1:
    temp = [rst3[0]]
    maxV = rst3[0][1]
    for i in range(1, len(rst3)):
        if maxV == rst3[i][1]:
            temp.append(rst3[i])
        else:
            break
    temp = sorted(temp, key=lambda x: x[0])

    if len(temp) == 1:
        rst3 = temp[0][0]
    else:
        rst3 = temp[1][0]
else:
    rst3 = rst3[0][0]



rst4 = sorted(dic.keys())
rst4 = rst4[-1] - rst4[0]

print(rst1)
print(rst2)
print(rst3)
print(rst4)
