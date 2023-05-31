from collections import deque
#
def bfs(x):
    global cnt, cntS
    copy_path = path[:]
    q = deque()
    q.append(x)
    cnt += 1
    copy_path[x] = -1

    while q:
        cx = q.popleft()
        if seat[cx] == 'S':
            cntS += 1
        for i in range(4):
            nx = cx + dr[i]
            if nx < 0 or nx > 24: continue
            if i == 0 or i == 2:
                if nx // 5 != cx // 5:
                    continue
            if copy_path[nx] == -1 or copy_path[nx] == 0: continue
            q.append(nx)
            copy_path[nx] = -1
            cnt += 1


def dfs(level):
    global cnt, cntS, ans
    if level == 25:
        if sum(path) == 7:
            cnt = 0
            cntS = 0
            for i in range(25):
                if path[i] == 1:
                    bfs(i)
                    break
            if cnt == 7 and cntS >= 4:
                ans += 1
        return
    if sum(path) > 7:
        return
    for i in range(2):
        path[level] = i
        dfs(level + 1)
        path[level] = 0



dr = [-1, -5, 1, 5]
seat = []
path = [0] * 25
for i in range(5):
    seat += list(input())

cnt = 0
cntS = 0
ans = 0
dfs(0)
print(ans)