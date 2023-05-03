import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((n, 0, str(n)))

    while q:
        current_p, time, root = q.popleft()
        if current_p == k:
            print(time)
            print(root)
            return 1

        # 좌로 걷기
        new_p = current_p - 1
        if new_p >= 0 and visited[new_p] == 0:
            visited[new_p] = 1
            q.append((new_p, time + 1, root + ' ' + str(new_p)))
        # 우로 걷기
        new_p = current_p + 1
        if new_p <= 100000 and visited[new_p] == 0:
            visited[new_p] = 1
            q.append((new_p, time + 1, root + ' ' + str(new_p)))

        # 순간이동하기기

        new_p = current_p * 2
        if new_p <= 100000 and visited[new_p] == 0:
            visited[new_p] = 1
            q.append((new_p, time + 1, root + ' ' + str(new_p)))


n, k = map(int, input().split())

visited = [0] * 100001

bfs()
