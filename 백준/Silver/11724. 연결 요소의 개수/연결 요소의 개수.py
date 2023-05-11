import sys
from collections import deque

input = sys.stdin.readline


def bfs(st):
    q = deque()
    q.append(st)
    path = [0] * (N + 1)
    path[st] = 1
    while q:
        cur_node = q.popleft()

        for i in arr[cur_node]:
            if path[i] == 1: continue
            path[i] = 1
            q.append(i)

    temp = []
    for i in range(1, N + 1):
        if path[i] == 1:
            temp.append(i)
    if temp in CC: return
    CC.append(temp)
    return


CC = []
N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N + 1):
    bfs(i)

print(len(CC))