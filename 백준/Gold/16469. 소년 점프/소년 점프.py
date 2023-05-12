import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    q = deque()
    q.append((y, x, 0))
    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1
    check[y][x] += 1
    while q:
        cy, cx, time = q.popleft()

        for i in range(4):
            ny = cy + my[i]
            nx = cx + mx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if maze[ny][nx] == 'B': continue
            if visited[ny][nx] == 1: continue
            visited[ny][nx] = 1
            check[ny][nx] += 1
            q.append((ny, nx, time + 1))
            if maze[ny][nx] < time + 1:
                maze[ny][nx] = time + 1


my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
N, M = map(int, input().rstrip().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
#
# if N == 2 and M == 2:
#     flag = 1
#     for i in range(3):
#         a, b = map(int, input().rstrip().split())
#     print(1)
#     print(1)



for i in range(N):
    for j in range(M):
        if maze[i][j] == 1:
            maze[i][j] = 'B'
for i in range(3):
    a, b = map(int, input().rstrip().split())
    bfs(a - 1, b - 1)

cnt = 0
minV = 99999
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'B' or check[i][j] != 3: continue
        if maze[i][j] < minV:
            minV = maze[i][j]

if minV == 99999:
    print(-1)
else:
    print(minV)
    for i in range(N):
        for j in range(M):
            if maze[i][j] == minV and check[i][j] == 3:
                cnt += 1
    print(cnt)
