def dfs(level):
    global ans
    if level == n:
        tot = 0
        for i in range(n):
            if path[i] == 1:
                tot += numbers[i]
        if tot == s and sum(path) >= 1:
            ans += 1

        return

    for i in range(2):
        path[level] = i
        dfs(level + 1)

n, s = map(int, input().split())

numbers = list(map(int, input().split()))

path = [0] * n
ans = 0
dfs(0)

print(ans)
