import sys

input = sys.stdin.readline

def dfs(x, level):
    global cnt
    for i in net[x]:
        if visited[i] == 1:
            continue
        visited[i] = 1
        cnt += 1
        dfs(i, level + 1)




n = int(input())
m = int(input())
net = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)
cnt = 0
visited = [0] * (n + 1)
visited[1] = 1
dfs(1, 0)
print(cnt)

