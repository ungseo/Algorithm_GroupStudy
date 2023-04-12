import sys

input = sys.stdin.readline

n = int(input().rstrip())
lst = []
for i in range(n):
    a, b = map(int, input().rstrip().split())
    lst.append([a, b])

lst.sort(key=lambda x:(x[1], x[0]))
cnt = 1
dft = lst[0][1]
for i in range(1,n):
    if dft <= lst[i][0]:
        dft = lst[i][1]
        cnt += 1

print(cnt)