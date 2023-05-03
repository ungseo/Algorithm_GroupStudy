import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((n, 0))

    while q:
        current_p, time = q.popleft()
        if current_p == k:
            print(time)
            return 1

        # 좌로 걷기
        new_p = current_p - 1
        if new_p >= 0 and visited[new_p] == 0 :
            visited[new_p] = 1
            q.append((new_p, time + 1))
        # 우로 걷기
        new_p = current_p + 1
        if new_p <= 100000 and visited[new_p] == 0:
            visited[new_p] = 1
            q.append((new_p, time + 1))

        # 순간이동하기기

        new_p = current_p * 2
        if new_p <= 100000 and visited[new_p] == 0:
            visited[new_p] = 1
            q.append((new_p, time + 1))


n, k = map(int, input().split())

visited = [0] * 100001

bfs()
