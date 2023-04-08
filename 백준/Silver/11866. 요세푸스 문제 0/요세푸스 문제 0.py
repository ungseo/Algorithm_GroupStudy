import sys

input = sys.stdin.readline

n, k = map(int, input().split())
gon = 0
lst = list(range(1, n + 1))
p = -1
print('<',end='')
while 1:
    cnt = 0
    while cnt != k:
        p += 1
        if p == n:
            p = 0
        if lst[p] != -1:
            cnt += 1

    if gon == n - 1:
        print(str(lst[p]), end='>')
        break

    print(str(lst[p]),end=', ')
    lst[p] = -1
    gon += 1