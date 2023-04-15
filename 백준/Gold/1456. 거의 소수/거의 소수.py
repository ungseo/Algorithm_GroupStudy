import sys

input = sys.stdin.readline

A, B = map(int, input().split())

M = B ** 0.5

prime = []
num = [1] * (int(M) + 1)
cnt = 0
for i in range(2, int(B ** 0.25) + 1):
    prime.append(i)
    for j in range(i + i, int(M) + 1, i):
        num[j] = 0
cnt = 0
for i in range(2,len(num)):
    if num[i] == 1:
        n = 2
        while 1:
            a = i ** n
            if a < A:
                n += 1
                continue
            if a > B:
                break
            n += 1
            cnt += 1

print(cnt)
