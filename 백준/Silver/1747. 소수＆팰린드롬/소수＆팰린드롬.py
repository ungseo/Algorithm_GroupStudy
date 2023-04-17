import sys

input = sys.stdin.readline

def is_pal(st):
    if st == st[::-1]:
        return 1
    return 0

n = input().rstrip()
l = len(n) + 1
n = int(n)

if l == 8:
    print(1003001)
else:
    limit = 10 ** l
    flag = 0
    nl = [1] * limit
    for i in range(2, limit):
        if nl[i] == 1 and i >= n:
            if is_pal(str(i)):
                print(i)
                flag = 1
                break
        for j in range(i + i, limit, i):
            if nl[j] == 0: continue
            if j % i == 0:
                nl[j] = 0
    if flag == 0:
        print(1000001)