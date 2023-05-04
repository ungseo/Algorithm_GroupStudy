import sys
from collections import deque

input = sys.stdin.readline

visited = [0] * 100001
a, b = map(int, input().split())
minSec = 21e8
q = deque()
q.append((a, 0))
visited[a] = 1
while q:
    cur_num, sec = q.popleft()


    if cur_num == b:
        if minSec > sec:
            minSec = sec

    new_num = cur_num * 2
    if new_num <= 100000 and visited[new_num] == 0:
        visited[new_num] = 1
        q.append((new_num, sec))

    new_num = cur_num - 1
    if new_num >= 0 and visited[new_num] == 0:
        visited[new_num] = 1
        q.append((new_num, sec + 1))

    new_num = cur_num + 1
    if new_num <= 100000 and visited[new_num] == 0:
        visited[new_num] = 1
        q.append((new_num, sec + 1))


print(minSec)
