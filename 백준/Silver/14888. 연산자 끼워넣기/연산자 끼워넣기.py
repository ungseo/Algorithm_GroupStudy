import sys

input = sys.stdin.readline


def dfs(level):
    if level == n - 1:
        tt = number[0]
        for i in range(level):
            if path[i] == 0:
                tt += number[i + 1]
            elif path[i] == 1:
                tt -= number[i + 1]
            elif path[i] == 2:
                tt *= number[i + 1]
            else:
                if tt < 0:
                    tt *= -1
                    tt //= number[i + 1]
                    tt *= -1
                else:
                    tt //= number[i + 1]

                    

        ans.append(tt)
        return

    for i in range(4):
        if calc[i] >= 1:
            calc[i] -= 1
            path[level] = i
            dfs(level + 1)
            calc[i] += 1
            path[level] = 0


n = int(input())

number = list(map(int, input().split()))

calc = list(map(int, input().split()))
path = [0] * (n - 1)
ans = []

dfs(0)
ans.sort()
print(ans[-1])
print(ans[0])
