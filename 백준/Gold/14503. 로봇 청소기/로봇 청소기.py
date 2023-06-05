import sys

input = sys.stdin.readline

def check(y, x):
    global ry, rx, d
    for i in range(4):
        ny = y + my[i]
        nx = x + mx[i]

        if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
        if floor[ny][nx] == 0:
            return 1
    return 0


my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
Y, X = map(int, input().split())
ry, rx, d = map(int, input().split())
floor = [list(map(int, input().split())) for _ in range(Y)]

room = 0
while 1:
    if floor[ry][rx] == 0:
        floor[ry][rx] = -1
        room += 1
    rst = check(ry, rx)
    if rst:
        for i in range(4):
            d -= 1
            if d == -1:
                d = 3
            ny = ry + my[d]
            nx = rx + mx[d]
            if floor[ny][nx] == 0:
                ry = ny
                rx = nx
                break
    else:
        ry -= my[d]
        rx -= mx[d]
        if floor[ry][rx] == 1:
            print(room)
            break



