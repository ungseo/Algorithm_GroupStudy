import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

q = deque()
q.append((n, 1))
ans = -1
while q:
    cur_x, times = q.popleft()
    if cur_x == m:
        ans = times
        break

    new_x1 = cur_x * 2
    if new_x1 <= m:
        q.append((new_x1, times + 1))
    new_x2 = cur_x * 10 + 1
    if new_x2 <= m:
        q.append((new_x2, times + 1))

print(ans)
