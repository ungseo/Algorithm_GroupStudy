import sys
from collections import deque

input = sys.stdin.readline


def melting():
    global ice
    copy_ice = []
    for i in range(Y):
        copy_ice.append(ice[i][:])

    for i in range(Y):
        for j in range(X):
            if ice[i][j] > 0:
                cnt = 0
                for d in range(4):
                    ny = i + my[d]
                    nx = j + mx[d]
                    if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
                    if ice[ny][nx] == 0:
                        cnt += 1
                copy_ice[i][j] -= cnt
                if copy_ice[i][j] < 0:
                    copy_ice[i][j] = 0
    ice = copy_ice


def check(y, x):
    q = deque()
    q.append((y, x))

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + my[i]
            nx = cx + mx[i]
            if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
            if copy_ice[ny][nx] == -1 or copy_ice[ny][nx] == 0: continue
            q.append((ny, nx))
            copy_ice[ny][nx] = -1


my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
Y, X = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(Y)]
time = 0
flag = 0
while 1:
    melting()
    time += 1
    copy_ice = []
    for i in range(Y):
        copy_ice.append(ice[i][:])

    land = 0
    for i in range(Y):
        for j in range(X):
            if copy_ice[i][j] > 0:
                copy_ice[i][j] = -1
                check(i, j)
                land += 1
                if land >= 2:
                    flag = 1
                    break
    if land == 0:
        flag = 2
        if flag:
            break

    if flag:
        break

if flag == 1:
    print(time)
else:
    print(0)
