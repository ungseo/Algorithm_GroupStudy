import sys
from collections import deque

input = sys.stdin.readline


def burning():
    q = deque()
    for i in fp:
        q.append(i)
    while q:
        cy, cx, time = q.popleft()

        for d in range(4):
            ny = cy + my[d]
            nx = cx + mx[d]

            if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
            if maze[ny][nx] == '#': continue
            if type(maze[ny][nx]) == int: continue

            q.append((ny, nx, time + 1))
            maze[ny][nx] = time + 1


def running(y, x):
    q = deque()
    q.append((y, x, 0))
    if maze[y][x] == 0: return 0
    visited = [[0] * X for _ in range(Y)]
    visited[y][x] = 1
    while q:
        cy, cx, time = q.popleft()

        for d in range(4):
            ny = cy + my[d]
            nx = cx + mx[d]

            if ny < 0 or nx < 0 or ny >= Y or nx >= X:
                return time + 1

            if maze[ny][nx] == '#': continue

            if type(maze[ny][nx]) == int and maze[ny][nx] <= time + 1: continue
            if visited[ny][nx] == 1: continue
            visited[ny][nx] = 1
            q.append((ny, nx, time + 1))
    return 0


my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
Y, X = map(int, input().rstrip().split())
maze = [list(input().rstrip()) for _ in range(Y)]

if Y == 1 or X == 1:
    print(1)

else:
    fp = []
    for i in range(Y):
        for j in range(X):
            if maze[i][j] == 'F':
                fy, fx = i, j
                fp.append((fy, fx, 0))
                maze[fy][fx] = 0
            if maze[i][j] == 'J':
                jy, jx = i, j

    burning()
    rst = running(jy, jx)

    if rst:
        print(rst)
    else:
        print('IMPOSSIBLE')
