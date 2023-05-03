import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x, safezone):
    q = deque()
    q.append((y, x, safezone))

    while q:
        nowy, nowx, nowsfz = q.popleft()
        if sea[nowy][nowx] == 1:
            saftyZone.append(nowsfz)
            return
        for i in range(8):
            ny = nowy + mvy[i]
            nx = nowx + mvx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
            if used[ny][nx] == 1: continue
            used[ny][nx] = 1
            q.append((ny, nx, nowsfz + 1))


mvy = [0, -1, -1, -1, 0, 1, 1, 1]
mvx = [-1, -1, 0, 1, 1, 1, 0, -1]
n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]

saftyZone = []
for i in range(n):
    for j in range(m):
        used = [[0] * m for _ in range(n)]
        used[i][j] = 1
        bfs(i, j, 0)

print(max(saftyZone))