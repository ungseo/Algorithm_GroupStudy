import sys

input = sys.stdin.readline


def bfs(idx, st):
    q = list()
    q.append((idx, st))

    while q:
        nidx, step = q.pop(0)
        if step == k:
            ans.append(nidx + 1)

        for i in lst[nidx]:
            if used[i] == 1: continue
            q.append((i, step + 1))
            used[i] = 1


n, m, k, x = map(int, input().split())
ans = []
lst = [[] for i in range(n)]
used = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    lst[a - 1].append(b - 1)

used[x - 1] = 1
bfs(x - 1, 0)

ans.sort()
#
# if k == 0:
#     print(x-1)
# else:
if ans:
    for i in ans:
        print(i)
else:
    print(-1)
