def dfs(level,p):
    if level == 3:
        rst = sum(path)
        if rst <= m:
            ans.append(rst)
        return

    for i in range(p, n):
        if used[i] == 1:continue
        path[level] = card[i]
        used[i] = 1
        dfs(level+1,i+1)
        used[i] = 0


n, m = map(int, input().split())
card = list(map(int, input().split()))
path = [0] * n
used = [0] * n
ans = []
dfs(0,0)

print(max(ans))