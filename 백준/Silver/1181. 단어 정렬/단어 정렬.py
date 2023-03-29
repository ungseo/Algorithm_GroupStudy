import sys

input = sys.stdin.readline
dic = {}
n = int(input().rstrip())
for _ in range(n):
    st = input().rstrip()
    if st in dic: continue
    else:
        dic[st] = len(st)
temp = sorted(dic.items(), key= lambda x: x[0])
temp.sort(key=lambda x: x[1])
for i in range(len(temp)):
    print(temp[i][0])