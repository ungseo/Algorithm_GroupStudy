import sys

input = sys.stdin.readline


def dfs(level, idx):
    global flag
    if flag == 1:
        return
    for i in arr[idx]:
        if used[i] == 1: continue
        if level == 3:
            flag = 1
            return
        used[i] = 1
        dfs(level + 1, i)
        used[i] = 0


n, m = map(int, input().split())
arr = [[]  for _ in range(n)]
used = [0] * n
flag = 0

if m < 4:
    print(flag)

else:
    for i in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(n):
        if arr[i]:
            used[i] = 1
            dfs(0, i)
            used[i] = 0
        if flag == 1:
            break

    print(flag)
