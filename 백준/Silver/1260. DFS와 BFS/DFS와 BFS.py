import sys

input = sys.stdin.readline

def dfs(st, level):
    print(st+1, end=' ')
    for i in arr[st]:
        if used[i] == 1: continue
        used[i] = 1
        dfs(i, level + 1)

def bfs():
    q = []
    q.append(v-1)
    while q:
        idx = q.pop(0)
        print(idx+1,end=' ')
        for i in arr[idx]:
            if used[i] == 1:continue
            used[i] = 1
            q.append(i)


n, m, v = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(m):
    s, e = map(int, input().split())
    arr[s-1].append(e-1)
    arr[e-1].append(s-1)

for i in arr:
    i.sort()



used = [0] * n
used[v-1] = 1
dfs(v-1, 0)
print()
used = [0] * n
used[v-1] = 1
bfs()