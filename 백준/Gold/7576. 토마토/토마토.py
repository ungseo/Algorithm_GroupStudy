import sys

input = sys.stdin.readline
from collections import deque


def bfs():
    while q:
        global days
        nowy, nowx, nowd = q.popleft()
        days = nowd
        for i in range(4):
            ny = nowy + mvy[i]
            nx = nowx + mvx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if tomato[ny][nx] != 0: continue
            tomato[ny][nx] = nowd + 1
            q.append((ny, nx, nowd + 1))


mvy = [-1, 0, 1, 0]
mvx = [0, 1, 0, -1]
M, N = map(int, input().split())
tomato = []
cnt = 0
for i in range(N):
    a = list(map(int, input().split()))
    tomato.append(a)
    if 0 not in a:
        cnt += 1
if cnt == N:
    print(0)

else:
    days = 0
    q = deque()
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                q.append((i, j, 0))
    bfs()
    flag = 1
    for i in range(N):
        if 0 in tomato[i]:
            flag = 0
            break

    if flag:
        print(days)
    else:
        print(-1)