import sys
input = sys.stdin.readline
n = int(input())
DAT = [0] * 10001
for i in range(n):
    DAT[int(input())] += 1
p = 1
cnt = 0
while cnt != n:
    if DAT[p] >= 1:
        DAT[p] -= 1
        cnt += 1
        print(p)
    else:
        p += 1


