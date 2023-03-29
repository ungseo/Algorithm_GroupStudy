import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    cnt = 0
    point = 0
    stack = list(input())
    while stack:
        ans = stack.pop(0)
        if ans == 'O':
            cnt += 1
            point += cnt
        else:
            cnt = 0

    print(point)