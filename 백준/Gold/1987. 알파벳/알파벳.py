import sys

## 65~ 90
input = sys.stdin.readline


def dfs(y, x, cnt):
    global max_cnt
    if cnt > max_cnt:
        max_cnt = cnt
    for i in range(4):
        ny = y + my[i]
        nx = x + mx[i]
        if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
        if check[ord(board[ny][nx])] == 1: continue
        check[ord(board[ny][nx])] = 1
        dfs(ny, nx, cnt + 1)
        check[ord(board[ny][nx])] = 0



my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
Y, X = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(Y)]
check = [0] * 91
max_cnt = 0

check[ord(board[0][0])] = 1
dfs(0, 0, 1)

print(max_cnt)