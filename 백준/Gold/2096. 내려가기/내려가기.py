import sys

input = sys.stdin.readline

n = int(input())

MAX = [0] * 3
MIN = [0] * 3
for _ in range(n):
    x, y, z = map(int, input().split())
    p = max(MAX[:2])
    q = max(MAX)
    r = max(MAX[1:])
    u = min(MIN[:2])
    i = min(MIN)
    o = min(MIN[1:])
    MAX[0] = x + p
    MAX[1] = y + q
    MAX[2] = z + r
    MIN[0] = x + u
    MIN[1] = y + i
    MIN[2] = z + o
print(max(MAX), min(MIN))

