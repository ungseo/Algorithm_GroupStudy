import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def bfs(y, x, mh):
    q = deque()
    q.append((y, x))

    while q:
        nowy, nowx = q.popleft()

        for i in range(4):
            ny = nowy + mvy[i]
            nx = nowx + mvx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            if wet[ny][nx] == -1: continue
            if ground[ny][nx] <= mh: continue
            wet[ny][nx] = -1
            q.append((ny, nx))



mvy = [0, 0, -1, 1]
mvx = [1, -1, 0, 0]
n = int(input())
ground = []

maxH = 0
for i in range(n):
    a = list(map(int, input().split()))
    if maxH < max(a):
        maxH = max(a)
    ground.append(a)

maxC = 0
for h in range(maxH - 1, -1, -1):
    wet = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if wet[i][j] == -1: continue
            if ground[i][j] > h:
                wet[i][j] = -1
                bfs(i, j, h)
                cnt += 1
    if maxC < cnt:
        maxC = cnt

print(maxC)