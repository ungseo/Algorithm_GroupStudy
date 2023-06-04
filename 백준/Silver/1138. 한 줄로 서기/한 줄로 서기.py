import sys

input = sys.stdin.readline


def dfs(level):
    if level == N:
        if path == [4, 2, 1, 3]:
            de = 1
        flag = 1
        for i in range(1, 1 + N):
            cnt = 0
            for j in range(N):
                if path[j] > i:
                    cnt += 1
                elif path[j] == i:
                    if cnt != memory[i - 1]:
                        flag = 0
                        break

        if flag == 1:
            print(*path)
        return

    for i in range(1, 1 + N):
        if visited[i] == 1: continue
        visited[i] = 1
        path[level] = i
        dfs(level + 1)
        visited[i] = 0


N = int(input())
memory = list(map(int, input().split()))

path = [0] * N
visited = [0] * (N + 1)
dfs(0)
