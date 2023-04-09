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
# pointer = 1
# me = 1
# roll = 0
# while maze[me] < 100:
#     go = [0] * 7
#     maxD = 0
#     maxidx = 0
#     for i in range(6, 0, -1):
#         pointer = me + i
#         if pointer > 100: continue
#         go[i] = maze[pointer]
#         if go[i] > maxD:
#             maxD = go[i]
#             maxidx = i
#     me = maxD
#     roll += 1
#     if maze[me] == 100:
#         break
#
# print(roll)
