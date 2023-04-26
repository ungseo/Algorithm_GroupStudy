from collections import deque


def bfs(start):
    q = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    cnt = 1

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                cnt += 1
                q.append(nx)

    return cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

result = []
max_cnt = 0

for i in range(1, N + 1):
    if graph[i]:
        cnt = bfs(i)
        if cnt > max_cnt:
            result = [i]
            max_cnt = cnt
        elif cnt == max_cnt:
            result.append(i)

print(*result)