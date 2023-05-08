import sys
from collections import deque

input = sys.stdin.readline


def bfs(x):
    q = deque()
    q.append((x, build_time[x]))
    tempAnswer = [0] * (n+1)
    tempAnswer[x] = build_time[x]
    while q:
        cur_node, cur_time = q.popleft()
        if tempAnswer[cur_node] > cur_time: continue
        for i in arr[cur_node]:
            if tempAnswer[i] > cur_time + build_time[i]: continue
            q.append((i, cur_time + build_time[i]))
            tempAnswer[i] = cur_time + build_time[i]
    return max(tempAnswer)



n = int(input())
arr = [[] for _ in range(n + 1)]
build_time = [0] * (n + 1)

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    build_time[i] = temp[0]
    for j in range(1, len(temp) - 1):
        arr[i].append(temp[j])

for i in range(1, n + 1):
    rst = bfs(i)
    print(rst)
