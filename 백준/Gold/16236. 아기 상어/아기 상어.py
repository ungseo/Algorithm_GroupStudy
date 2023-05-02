import sys
from collections import deque

input = sys.stdin.readline


def findShark():
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                return i, j


def findmeat(y, x, sec):
    global eat, size
    q = deque()
    q.append((y, x, sec))
    alst = []
    while q:
        nowy, nowx, nowsec = q.popleft()
        if 0 < sea[nowy][nowx] < size:
            alst.append((nowy, nowx, nowsec))
        if alst:
            if alst[0][2] < nowsec:
                break
        for i in range(4):
            ny = nowy + mvy[i]
            nx = nowx + mvx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            if used[ny][nx] == 1: continue
            if sea[ny][nx] > size: continue
            used[ny][nx] = 1
            q.append((ny, nx, nowsec + 1))
    if alst:
        alst.sort(key=lambda x: (x[2], x[0]))
        eat += 1
        if eat == size:
            size += 1
            eat = 0
        return alst[0]
    return -1,-1,sec



n = int(input())

sea = [list(map(int, input().split())) for _ in range(n)]
used = [[0] * n for _ in range(n)]
mvy = [-1, 0, 1, 0]
mvx = [0, -1, 0, 1]
st, ed = findShark()
secc = 0
size = 2
eat = 0
used[st][ed] = 1
sea[st][ed] = 0

while 1:
    st, ed, secc = findmeat(st, ed, secc)
    if st == -1 and ed == -1:
        print(secc)
        break
    used = [[0] * n for _ in range(n)]
    used[st][ed] = 1
    sea[st][ed] = 0
