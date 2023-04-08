import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    que = list(map(int, input().split()))
    p = m
    que = deque(que)
    cnt = 0
    while 1:
        priority = max(que)
        a = que.popleft()

        if a == priority:
            cnt += 1
            if p == 0 or p == -1:
                print(cnt)
                break

        else:
            que.append(a)

        p -= 1
        if p == -1:
            p = len(que) -1


