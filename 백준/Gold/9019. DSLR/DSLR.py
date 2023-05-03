import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end):
    q = deque([(start, '')])  # (현재 숫자, 지금까지 이루어진 명령어)
    visited = set()  # 방문한 숫자 집합
    visited.add(start)

    while q:
        cur, command = q.popleft()

        if cur == end:
            return command

        # D 명령어 수행
        next_num = (cur * 2) % 10000
        if next_num not in visited:
            visited.add(next_num)
            q.append((next_num, command+'D'))

        # S 명령어 수행
        next_num = cur - 1 if cur != 0 else 9999
        if next_num not in visited:
            visited.add(next_num)
            q.append((next_num, command+'S'))

        # L 명령어 수행
        next_num = (cur % 1000) * 10 + (cur // 1000)
        if next_num not in visited:
            visited.add(next_num)
            q.append((next_num, command+'L'))

        # R 명령어 수행
        next_num = (cur % 10) * 1000 + (cur // 10)
        if next_num not in visited:
            visited.add(next_num)
            q.append((next_num, command+'R'))


T = int(input().strip())

for _ in range(T):
    start, end = map(int, input().strip().split())
    result = bfs(start, end)
    print(result)
