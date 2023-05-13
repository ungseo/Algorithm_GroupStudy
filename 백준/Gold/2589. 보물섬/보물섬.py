import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x, dis):
    global maxDis
    q = deque()
    q.append((y, x, dis))
    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1
    while q:
        cy, cx, dis = q.popleft()
        if dis > maxDis:
            maxDis = dis

        for i in range(4):
            ny = cy + my[i]
            nx = cx + mx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if visited[ny][nx] == 1: continue
            if board[ny][nx] == 'W': continue
            visited[ny][nx] = 1
            q.append((ny, nx, dis + 1))



my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

maxDis = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            bfs(i, j, 0)


print(maxDis)