def dfs(lv):
    global cnt
    if lv == n:
        cnt += 1
        return

    for i in range(n):
        if used[i] == 1:continue
        if dae1[lv+i] == 1: continue
        if dae2[lv-i+n-1] == 1:continue

        used[i] = 1
        dae1[lv+i] = 1
        dae2[lv-i+n-1] = 1
        dfs(lv + 1)
        used[i] = 0
        dae1[lv + i] = 0
        dae2[lv - i + n - 1] = 0





n = int(input())
used = [0] * n
dae1 = [0] * n**2
dae2 = [0] * n**2
cnt = 0

dfs(0)

print(cnt)