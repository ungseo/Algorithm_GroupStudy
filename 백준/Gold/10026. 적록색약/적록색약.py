import sys
from collections import deque

input = sys.stdin.readline


def bfs(color, y, x):
    global cnt
    q = deque()
    q.append((y, x))
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            ny = nowy + movy[i]
            nx = nowx + movx[i]
            if 0 > ny or ny >= n: continue
            if 0 > nx or nx >= n: continue
            if used[ny][nx] == 1: continue
            if dist[ny][nx] != color: continue
            used[ny][nx] = 1
            q.append((ny, nx))

    cnt += 1


def dbfs(color, y, x):
    global disabled_cnt
    q = deque()
    q.append((y, x))
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            ny = nowy + movy[i]
            nx = nowx + movx[i]
            if 0 > ny or ny >= n: continue
            if 0 > nx or nx >= n: continue
            if dused[ny][nx] == 1: continue
            if color == 'R' and dist[ny][nx] == 'B': continue
            if color == 'G' and dist[ny][nx] == 'B': continue
            if color == 'B' and dist[ny][nx] != 'B': continue
            dused[ny][nx] = 1
            q.append((ny, nx))
    disabled_cnt += 1


movy = [-1, 0, 1, 0]
movx = [0, 1, 0, -1]
n = int(input())
cnt = 0
disabled_cnt = 0
dist = [list(input()) for _ in range(n)]
used = [[0] * n for _ in range(n)]
dused = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if used[i][j] == 0:
            used[i][j] = 1
            bfs(dist[i][j], i, j)
        if dused[i][j] == 0:
            dused[i][j] = 1
            dbfs(dist[i][j], i, j)

print(cnt, disabled_cnt)
