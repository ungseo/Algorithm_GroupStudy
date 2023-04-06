import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    global cnt
    q = deque()
    q.append((y, x))

    while q:
        nowy, nowx = q.popleft()
        for i in range(8):
            ny = nowy + movy[i]
            nx = nowx + movx[i]
            if ny < 0 or ny >= h: continue
            if nx < 0 or nx >= w: continue
            if used[ny][nx] == 1: continue
            if island[ny][nx] == 0: continue
            q.append((ny, nx))
            used[ny][nx] = 1
    cnt += 1



movy = [-1, 0, 1, 0, -1, 1, 1, -1]
movx = [0, 1, 0, -1, 1, 1, -1, -1]
while 1:
    cnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    used = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if used[i][j] == 1: continue
            if island[i][j] == 0: continue
            used[i][j] = 1
            bfs(i, j)
    print(cnt)