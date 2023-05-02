import sys
from collections import deque

input = sys.stdin.readline


def bfs(s, e):
    global flag
    q = deque()
    q.append(s)

    while q:
        nowcity = q.popleft()
        if nowcity == e:
            return
        for i in range(1, 1 + n):
            if arr[nowcity][i] == 0: continue
            if used[i] == 1: continue
            q.append(i)
            used[i] = 1
    flag = 0
    return

n = int(input())
m = int(input())

arr = [[0]] + [[0] + list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

flag = 1
for i in range(len(plan) - 1):
    st, ed = plan[i], plan[i + 1]
    used = [0] * (n + 1)
    used[st] = 1
    bfs(st, ed)

if flag:
    print('YES')
else:
    print('NO')