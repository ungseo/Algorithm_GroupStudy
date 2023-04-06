import sys

input = sys.stdin.readline

a, b, v = map(int, input().split())
# v- a == 마지막날을 뺀 목표값 , a - b == 하루에 갈수있는 순 거리
goal = v - a
f_day = goal / (a-b)
if f_day > int(f_day):
    f_day = int(f_day) + 1
else:
    f_day = int(f_day)


print(f_day+1)
