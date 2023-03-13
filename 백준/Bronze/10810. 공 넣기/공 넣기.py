n, m = map(int, input().split())
lst = [0] * n
for s in range(m):
    i, j, k = map(int, input().split())
    for D in range(i - 1, j):
        lst[D] = k

print(*lst)
