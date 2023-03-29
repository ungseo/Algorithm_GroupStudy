import sys

input = sys.stdin.readline


def bfs(step, idx):
    q = []
    q.append((step, idx))

    while q:
        nstep, nidx = q.pop(0)
        if nidx == s - 1:
            return nstep
        for i in range(n):
            if used[i] == 1: continue
            if arr[nidx][i] == 1:
                q.append((nstep + 1, i))
                used[i] = 1
    return -1

n = int(input())
used = [0] * n
f, s = map(int, input().split())
m = int(input())
arr = [[0] * n for _ in range(n)]
ans = []
for _ in range(m):
    mom, son = map(int, input().split())
    arr[mom - 1][son - 1] = 1
    arr[son - 1][mom - 1] = 1
used[f - 1] = 1
rst = bfs(0, f - 1)
print(rst)