import sys

input = sys.stdin.readline


def dfs(y, x, level, hap):
    global maxSum
    if level == 3:
        if maxSum < hap:
            maxSum = hap
        return
    for i in range(4):
        ny = y + mvy[i]
        nx = x + mvx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
        if used[ny][nx] == 1: continue
        used[ny][nx] = 1
        dfs(ny, nx, level + 1, hap + tetris[ny][nx])
        used[ny][nx] = 0


mvy = [-1, 0, 1, 0]
mvx = [0, 1, 0, -1]
n, m = map(int, input().split())
tetris = [list(map(int, input().split())) for _ in range(n)]
maxSum = 0
used = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        used[i][j] = 1
        dfs(i, j, 0, tetris[i][j])
        used[i][j] = 0


# 뻐큐 위아래
for i in range(n):
    for j in range(m - 2):
        tsum = 0
        if i != n - 1:
            tsum += tetris[i][j] + tetris[i][j + 1] + tetris[i][j + 2] + tetris[i + 1][j + 1]
            if maxSum < tsum:
                maxSum = tsum
        else:
            tsum += tetris[i][j] + tetris[i][j + 1] + tetris[i][j + 2] + tetris[i - 1][j + 1]
            if maxSum < tsum:
                maxSum = tsum
            continue
        if i != 0:
            tsum1 = tsum - tetris[i + 1][j + 1] + tetris[i - 1][j + 1]
            if maxSum < tsum1:
                maxSum = tsum1

# 뻐큐 오른쪽
for i in range(n - 2):
    for j in range(m - 1):
        tsum = 0
        tsum += tetris[i][j] + tetris[i + 1][j] + tetris[i + 2][j] + tetris[i + 1][j + 1]
        if maxSum < tsum:
            maxSum = tsum

# 뻐큐 왼쪽
for i in range(n - 2):
    for j in range(1, m):
        tsum = 0
        tsum += tetris[i + 1][j - 1] + tetris[i][j] + tetris[i + 1][j] + tetris[i + 2][j]
        if maxSum < tsum:
            maxSum = tsum

print(maxSum)
