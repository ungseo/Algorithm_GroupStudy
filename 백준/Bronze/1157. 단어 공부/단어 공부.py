import sys

input = sys.stdin.readline

st = list(input().rstrip().upper())

dic = {}

for i in range(len(st)):
    if st[i] in dic:
        dic[st[i]] += 1
    else:
        dic[st[i]] = 1
rst = sorted(dic.items(), key=lambda x: x[1], reverse=True)


if len(rst) != 1:
    rst1 = rst[0][1]
    rst2 = rst[1][1]

    if rst1 == rst2:
        print('?')

    else:
        print(rst[0][0])
else:
    print(st[0].upper())
