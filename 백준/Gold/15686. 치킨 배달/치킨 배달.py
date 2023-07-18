import sys
input = sys.stdin.readline


def bfs(y, x, lst):
    min = 21e8
    for i in range(M):
        a, b = store_list[lst[i]]

        chic_dis = abs(y-a) + abs(x-b)
        if chic_dis < min:
            min = chic_dis
    return min

def dfs(level):
    if level == M:
        temp = []
        for i in range(M):
            temp.append(path[i])
        alive_store.append(temp)
        return

    for i in range(branch):
        if used[i] == 1: continue
        if level > 0 and path[level - 1] >= i: continue
        used[i] = 1
        path[level] = i
        dfs(level + 1)
        used[i] = 0


my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
store_list = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            store_list.append((i, j))

branch = len(store_list)
alive_store = []
path = [0] * M
used = [0] * branch
dfs(0)

total = 21e8
for s in range(len(alive_store)):
    temp_total = 0
    flag = 1
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                temp_total += bfs(i, j, alive_store[s])
                if temp_total > total:
                    flag = 0
                    break
        if flag == 0:
            break
    if total > temp_total:
        total = temp_total

print(total)
