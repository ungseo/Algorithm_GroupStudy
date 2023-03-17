import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    temp = lst[i-1:j]
    temp = temp[::-1]
    n = 0
    for s in range(i-1,j):
        lst[s] = temp[n]
        n += 1


print(*lst)
