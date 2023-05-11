import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    global cnt
    q = deque()
    q.append((y, x))

    while q:
        c_y, c_x = q.popleft()

        for i in range(4):
            ny = c_y + my[i]
            nx = c_x + mx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if farm[ny][nx] == 0: continue
            farm[ny][nx] = 0
            q.append((ny, nx))
    cnt += 1


T = int(input())
my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
for tc in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                bfs(i, j)
    print(cnt)
