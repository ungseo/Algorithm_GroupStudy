import sys

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    R, S = input().split()
    lst = list(S)
    for i in range(len(lst)):
        lst[i] = lst[i] * int(R)
    print(''.join(lst))
