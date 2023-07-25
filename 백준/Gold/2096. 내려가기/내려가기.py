import sys

input = sys.stdin.readline

n = int(input())

ANS = [(0, 0)] * 3
for _ in range(n):
    x, y, z = map(int, input().split())
    p = max(ANS[0][0], ANS[1][0])
    q = max(ANS[0][0], ANS[1][0], ANS[2][0])
    r = max(ANS[1][0], ANS[2][0])
    u = min(ANS[0][1], ANS[1][1])
    i = min(ANS[0][1], ANS[1][1], ANS[2][1])
    o = min(ANS[1][1], ANS[2][1])
    ANS[0] = (x + p, x + u)
    ANS[1] = (y + q, y + i)
    ANS[2] = (z + r, z + o)

print(max(ANS[0][0], ANS[1][0], ANS[2][0]), min(ANS[0][1], ANS[1][1], ANS[2][1]))
