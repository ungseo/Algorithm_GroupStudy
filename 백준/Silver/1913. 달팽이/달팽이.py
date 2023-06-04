import sys

input = sys.stdin.readline

my = [1, 0, -1, 0]
mx = [0, 1, 0, -1]
N = int(input())
F = int(input())
board = [[0] * N for _ in range(N)]

n = N ** 2
y, x = 0, 0
dr = 0

while 1:
    board[y][x] = n
    if n == F:
        ay, ax = y + 1, x + 1
    n -= 1
    ny = my[dr] + y
    nx = mx[dr] + x
    if ny < 0 or nx < 0 or ny >= N or nx >= N or board[ny][nx] > 0:
        dr += 1
        dr %= 4
    y = my[dr] + y
    x = mx[dr] + x
    if n == 0:
        break

for i in range(N):
    for j in range(N):
        print(board[i][j], end=' ')
    print()

print(ay, ax)

