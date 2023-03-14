import sys

input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append((int(input()), i))
a = sorted(lst, key=lambda x: x[0])

maxV = 0
for i in range(n):
    if maxV < a[i][1] - i:
        maxV = a[i][1] - i

print(maxV + 1)