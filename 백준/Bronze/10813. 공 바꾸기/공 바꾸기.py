import sys

input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(range(1,1+n))
for s in range(m):
    i, j = map(int, input().split())
    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]

print(*lst)