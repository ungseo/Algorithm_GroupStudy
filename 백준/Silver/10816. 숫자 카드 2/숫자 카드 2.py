import sys

input = sys.stdin.readline

n = int(input())
DAT = [0] * 20000002
card = list(map(int, input().split()))

for i in card:
    DAT[i + 10000000] += 1
m = int(input())
fcard = list(map(int, input().split()))

for i in range(m):
    print(DAT[fcard[i] + 10000000],end=' ')
