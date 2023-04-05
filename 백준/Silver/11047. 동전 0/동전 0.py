import sys

input = sys.stdin.readline

wallet = []
n, k = map(int, input().split())
for i in range(n):
    a = int(input())
    if a <= k:
        wallet.append(a)

wallet.sort(reverse=True)
cnt = 0
idx = 0
while idx < len(wallet):
    if k - wallet[idx] < 0:
        idx += 1
    else:
        cnt += 1
        k -= wallet[idx]
    if k == 0:
        break

print(cnt)