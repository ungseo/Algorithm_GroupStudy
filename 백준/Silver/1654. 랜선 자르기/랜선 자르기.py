import sys

input = sys.stdin.readline

k, n = map(int, input().split())

LAN = []
for i in range(k):
    LAN.append(int(input()))

LAN.sort()

st = 1
ed = LAN[-1]
mid = (st + ed) // 2
ans = []
while st <= ed:
    if mid == 0:
        break
    cnt = 0
    for i in range(len(LAN)):
        cnt += LAN[i] // mid
    if cnt >= n:
        ans.append(mid)
        st = mid + 1
        mid = (st + ed) // 2

    else:
        ed = mid - 1
        mid = (st + ed) // 2


print(max(ans))

