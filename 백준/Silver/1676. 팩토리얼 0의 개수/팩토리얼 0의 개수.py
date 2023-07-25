import sys

input = sys.stdin.readline


def factorial(numb):
    if numb <= 1:
        return 1

    return numb * factorial(numb - 1)


rst = factorial(int(input()))

cnt = 0
while 1:
    if rst % 10 == 0:
        cnt += 1
    else:
        break
    rst //= 10

print(cnt)