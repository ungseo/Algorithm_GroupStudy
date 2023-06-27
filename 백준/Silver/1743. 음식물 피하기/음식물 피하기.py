import sys
from collections import deque

input = sys.stdin.readline


def bfs(a, b, t):
    q = deque()
    q.append((a, b))
    cnt = t
    while q:
        cy, cx= q.popleft()

        for dr in range(4):
            ny = cy + my[dr]
            nx = cx + mx[dr]
            if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
            if visited[ny][nx] == 1: continue
            if floor[ny][nx] == '.': continue
            visited[ny][nx] = 1
            q.append((ny, nx))
            cnt += 1
    return cnt


my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]

Y, X, N = map(int, input().split())

floor = [['.'] * X for _ in range(Y)]
visited = [[0] * X for _ in range(Y)]
for i in range(N):
    y, x = map(int, input().split())
    floor[y - 1][x - 1] = '#'

maxTrash = 0
for i in range(Y):
    for j in range(X):
        if floor[i][j] == '#':
            visited[i][j] = 1
            rst = bfs(i, j, 1)
            if rst > maxTrash:
                maxTrash = rst

print(maxTrash)
