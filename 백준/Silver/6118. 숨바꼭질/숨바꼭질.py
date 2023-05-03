import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((1, 0))
    maxV = 0
    while q:
        current_node, distance = q.popleft()
        if maxV < distance:
            maxV = distance
            maxIdx = current_node
        for i in range(len(farm[current_node])):
            if used[farm[current_node][i]] == 1: continue
            smell[farm[current_node][i]] = distance + 1
            q.append((farm[current_node][i], distance + 1))
            used[farm[current_node][i]] = 1
    return maxV


n, m = map(int, input().split())
farm = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    farm[a].append(b)
    farm[b].append(a)

used = [0] * (n + 1)
used[1] = 1
smell = [0] * (n + 1)

ans1 = 0
ans2 = bfs()
ans3 = 0
for i in range(n, 0, -1):
    if smell[i] == ans2:
        ans3 += 1
        ans1 = i

print(ans1, ans2, ans3)