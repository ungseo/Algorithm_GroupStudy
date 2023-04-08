import sys

input = sys.stdin.readline

while 1:
    lst = list(map(int, input().split()))
    lst.sort()
    if lst == [0,0,0]:
        break
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        print('right')
    else:
        print('wrong')