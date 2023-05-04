import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    global minSec
    q = deque()
    q.append((a, 0))
    visited = [0] * 100001
    visited[a] = 1
    visited[b] = -1
    record = dict()
    while q:
        cur_num, sec = q.popleft()
        visited[cur_num] = 1
        if minSec < sec:
            return record

        if cur_num == b:
            minSec = sec
            if sec not in record:
                record[sec] = 1
            else:
                record[sec] += 1
            visited[cur_num] = -1

        new_num = cur_num * 2
        if new_num <= 100000 and visited[new_num] != 1:
            q.append((new_num, sec + 1))

        new_num = cur_num - 1
        if new_num >= 0 and visited[new_num] != 1:
            q.append((new_num, sec + 1))

        new_num = cur_num + 1
        if new_num <= 100000 and visited[new_num] != 1:
            q.append((new_num, sec + 1))


a, b = map(int, input().split())
minSec = 21e8
ans = bfs()
ans = list(ans.items())[0]
print(ans[0])
print(ans[1])

