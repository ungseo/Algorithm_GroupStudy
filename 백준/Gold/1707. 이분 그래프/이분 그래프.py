import sys
from collections import deque

input = sys.stdin.readline


# 색칠 함수
def bfs(x):
    global flag
    q = deque()
    q.append((x, 'R'))

    while q:
        nidx, color = q.popleft()
        if color == 'R':
            nC = 'B'
        else:
            nC = 'R'

        for i in range(len(arr[nidx])):

            if used[arr[nidx][i]] != 0:
                arr[nidx][i] = used[arr[nidx][i]]
            else:
                q.append((arr[nidx][i], nC))
                used[arr[nidx][i]] = nC
                arr[nidx][i] = nC


T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    used = [0] * (V + 1)
    for i in range(1, V+1):
        if used[i] == 0:
            used[i] = 'R'
            bfs(i)
    flag = 1

    for i in range(1, V + 1):
        if used[i] in arr[i]:
            flag = 0
            break

    if flag:
        print('YES')
    else:
        print('NO')
