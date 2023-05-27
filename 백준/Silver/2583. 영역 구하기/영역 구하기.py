import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline


def dfs(y, x):
    global size
    for i in range(4):
        ny = y + my[i]
        nx = x + mx[i]
        if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
        if paper[ny][nx] == 0:
            paper[ny][nx] = 1
            size += 1
            dfs(ny,nx)

my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
Y, X, K = map(int, input().split())
paper = [[0] * X for _ in range(Y)]

for i in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            paper[i][j] = 1

cnt = 0
sizeList = []
for i in range(Y):
    for j in range(X):
        if paper[i][j] == 0:
            paper[i][j] = 1
            size = 1
            dfs(i, j)
            cnt += 1
            sizeList.append(size)

sizeList.sort()
print(cnt)
print(*sizeList)
