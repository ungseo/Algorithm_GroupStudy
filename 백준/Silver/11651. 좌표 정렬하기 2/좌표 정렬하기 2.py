import sys

input = sys.stdin.readline
lst = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    lst.append([x, y])

lst.sort(key=lambda x:x[0])
lst.sort(key=lambda x:x[1])
for i in lst:
    print(*i)
