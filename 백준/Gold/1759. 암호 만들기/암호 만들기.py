import sys

input = sys.stdin.readline


def dfs(level, idx):
    if level == L:
        mcnt = 0
        for i in range(L):
            if path[i] in mo:
                mcnt += 1
        if mcnt > 0 and L-mcnt > 1:
            print(''.join(path))
        return

    for i in range(idx, C):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = pw[i]
        dfs(level + 1, i + 1)
        used[i] = 0


L, C = map(int, input().split())
pw = list(input().split())
pw.sort()
path = [0] * L
used = [0] * C
mo = ['a','e','i','o','u']
dfs(0, 0)
