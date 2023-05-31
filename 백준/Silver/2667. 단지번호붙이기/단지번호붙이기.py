import sys ,heapq

input = sys.stdin.readline


def dfs(y, x):
    global cnt
    for i in range(4):
        ny = y + my[i]
        nx = x + mx[i]
        if ny < 0 or nx < 0 or nx >= N or ny >= N: continue
        if city[ny][nx] != 1: continue
        city[ny][nx] = 2
        cnt += 1
        dfs(ny, nx)

my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]
N = int(input().rstrip())
city = [list(map(int, input().rstrip())) for _ in range(N)]
ansList = []
group = 0
for i in range(N):
    for j in range(N):
        if city[i][j] ==1:
            cnt = 1
            city[i][j] = 2
            dfs(i, j)
            heapq.heappush(ansList, cnt)
            group += 1

print(group)
for i in range(group):
    print(heapq.heappop(ansList))