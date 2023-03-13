import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

maxV = -1000000
minV = 1000000
for i in lst:
    if maxV < i:
        maxV = i
    if minV > i:
        minV = i

print(f'{minV} {maxV}')
