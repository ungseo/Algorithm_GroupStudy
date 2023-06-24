import sys

input = sys.stdin.readline

n = int(input())
arr = [0]

for i in range(n):
    arr.append(int(input()))

dp = [[0, 0, 0] for _ in range(n + 1)]

for i in range(n):
    rst0 = max(dp[i][1], dp[i][2])
    dp[i+1][0] = rst0
    dp[i+1][1] = dp[i][0] + arr[i+1]
    dp[i+1][2] = dp[i][1] + arr[i+1]

print(max(dp[n][1], dp[n][2]))