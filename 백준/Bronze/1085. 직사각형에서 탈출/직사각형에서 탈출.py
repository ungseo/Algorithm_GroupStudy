import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().split())

ans_lst = [a1, a2, a3, a4] = [x-0, w-x, y-0, h-y]
print(min(ans_lst))
