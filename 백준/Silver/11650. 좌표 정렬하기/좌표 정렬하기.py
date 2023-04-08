import sys

input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    a, b = map(int,input().split())
    lst.append([a, b])

lst.sort(key=lambda x:x[1])
lst.sort(key=lambda x:x[0])

for i in range(n):
    print(*lst[i])