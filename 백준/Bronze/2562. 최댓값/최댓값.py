import sys

input = sys.stdin.readline

maxI = 1
maxV = 0
for i in range(1,10):
    n = int(input())
    if maxV < n:
        maxV = n
        maxI = i

print(maxV)
print(maxI)