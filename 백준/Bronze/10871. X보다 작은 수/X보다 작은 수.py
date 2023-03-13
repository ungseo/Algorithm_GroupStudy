import sys

n, x = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

for i in lst:
    if i < x:
        print(i, end=' ')