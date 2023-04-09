import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((1, 0))

    while q:
        me, roll = q.popleft()
        if me == 100:
            ans.append(roll)
        for i in range(1, 7):
            nme = me + i
            if nme > 100: continue
            if used[nme] == 1: continue
            used[nme] = 1
            q.append((maze[nme], roll + 1))


N, M = map(int, input().split())
used = [0] * 101
maze = list(range(101))
ans = []
for i in range(N + M):
    st, ed = map(int, input().split())
    maze[st] = ed
bfs()
print(min(ans))
