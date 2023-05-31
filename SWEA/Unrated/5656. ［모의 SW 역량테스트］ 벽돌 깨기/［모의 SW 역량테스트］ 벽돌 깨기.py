
def sort_MAP():
    for i in range(X):
        n = Y - 1
        flag = 1
        while n != 0:
            if copyMAP[n][i] > 0:
                n -= 1
            else:  # 0 찾으면
                fn = n - 1
                while fn != -1:
                    if copyMAP[fn][i] > 0:
                        copyMAP[n][i], copyMAP[fn][i] = copyMAP[fn][i], copyMAP[n][i]
                        break
                    else:
                        fn -= 1
                        if fn == -1:
                            flag = 0
                            break
            if flag == 0:
                break


def break_bricks(y, x):
    global cnt, copyMAP
    rg = copyMAP[y][x]
    copyMAP[y][x] = 0
    cnt += 1
    for i in range(4):
        for d in range(1, rg):
            ny = y + my[i] * d
            nx = x + mx[i] * d

            if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
            if copyMAP[ny][nx] == 0: continue
            break_bricks(ny, nx)


def dfs(level):
    global cnt, copyMAP, bricks
    if level == N:
        cnt = 0
        copyMAP = []
        for i in range(Y):
            copyMAP.append(MAP[i][:])
        for i in range(N):
            n = 0
            while n < Y:
                if copyMAP[n][path[i]] == 0:
                    n += 1
                    continue
                else:
                    break_bricks(n, path[i])
                    sort_MAP()
                    break
        ans.append(bricks-cnt)
        return

    for i in range(X):
        if i == 6:
            de = 1
        if used[i] == 1: continue
        path[level] = i
        dfs(level + 1)


T = int(input())
my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
for tc in range(1, T + 1):
    N, X, Y = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(Y)]
    path = [0] * N
    used = [0] * X
    ans = []
    cnt = 0
    bricks = 0
    for i in range(Y):
        for j in range(X):
            if MAP[i][j] > 0:
                bricks += 1
    dfs(0)
    print(f'#{tc} {min(ans)}')
