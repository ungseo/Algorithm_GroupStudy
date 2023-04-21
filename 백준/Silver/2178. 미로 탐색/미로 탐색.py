import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((0, 0, 1))

    while q:
        nowy, nowx, step = q.popleft()

        for i in range(4):
            ny = mvy[i] + nowy
            nx = mvx[i] + nowx
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if maze[ny][nx] == 0: continue
            if maze[ny][nx] == 1:
                q.append((ny, nx, step + 1))
                maze[ny][nx] = step+1

    return maze[N-1][M-1]


mvy = [-1, 0, 1, 0]
mvx = [0, 1, 0, -1]
N, M = map(int, input().rstrip().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs())



