import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    while q:
        global day
        nowy, nowx, nowf, nowd = q.popleft()
        day = nowd
        for i in range(4):
            ny = nowy + mvy[i]
            nx = nowx + mvx[i]
            if ny < 0 or nx < 0 or ny >= M or nx >= N: continue
            if tomato[nowf][ny][nx] == 0:
                tomato[nowf][ny][nx] = nowd + 1
                q.append((ny, nx, nowf, nowd + 1))

        if nowf + 1 < H and tomato[nowf + 1][nowy][nowx] == 0:
            tomato[nowf + 1][nowy][nowx] = nowd + 1
            q.append((nowy, nowx, nowf + 1, nowd + 1))
        if nowf - 1 >= 0 and tomato[nowf - 1][nowy][nowx] == 0:
            tomato[nowf - 1][nowy][nowx] = nowd + 1
            q.append((nowy, nowx, nowf - 1, nowd + 1))


mvy = [-1, 0, 1, 0]
mvx = [0, 1, 0, -1]
N, M, H = map(int, input().split())
tomato = []
cnt = 0
for h in range(H):
    temp = []
    for i in range(M):
        a = list(map(int, input().split()))
        temp.append(a)
        if 0 not in a:
            cnt += 1
    tomato.append(temp)

if cnt == M * H:
    print(0)

else:
    q = deque()
    day = 0
    flag = 0
    for h in range(H):
        for i in range(M):
            for j in range(N):
                if tomato[h][i][j] == 1:
                    q.append((i, j, h, 1))
                    flag = 1
    bfs()

    if flag == 1:

        for h in range(H):
            for i in range(M):
                if 0 in tomato[h][i]:
                    print(-1)
                    flag = 0
                    break
            if flag == 0:
                break
        if flag == 1:
            print(day - 1)
    else:
        print(-1)