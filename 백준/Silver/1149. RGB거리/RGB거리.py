import sys

input = sys.stdin.readline

n = int(input())
RGB = []
for i in range(n):
    RGB.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(n)]
dp[0][0] = RGB[0][0]
dp[0][1] = RGB[0][1]
dp[0][2] = RGB[0][2]

for i in range(1, n):
    dp[i][0] = RGB[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = RGB[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = RGB[i][2] + min(dp[i-1][0], dp[i-1][1])


print(min(dp[n-1]))
