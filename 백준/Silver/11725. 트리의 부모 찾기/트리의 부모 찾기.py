import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x):
    for i in tree[x]:
        if check[i] > 0: continue
        check[i] = x
        dfs(i)


n = int(input())

tree = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

check = [0] * (n + 1)
check[1] = 1

dfs(1)

for i in range(2, n + 1):
    print(check[i])
