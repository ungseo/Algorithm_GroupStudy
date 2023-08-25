import sys
from collections import deque

input = sys.stdin.readline

my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    maxW = 1
    while q:
        cy, cx = q.popleft()

        for dr in range(4):
            ny = cy + my[dr]
            nx = cx + mx[dr]
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
            if paper[ny][nx] == 0: continue
            if visited[ny][nx] == 1: continue
            q.append((ny, nx))
            visited[ny][nx] = 1
            maxW += 1
    ansW.append(maxW)


n, m = map(int, input().split())

paper = []

for _ in range(n):
    paper.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]

ansCnt = 0
ansW = []
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and visited[i][j] == 0:
            ansCnt += 1
            bfs(i, j)

print(ansCnt)
if ansW:
    
    print(max(ansW))
else: 
    print(0)