import sys

input = sys.stdin.readline


def uclide(a, b):

    r = a % b
    while 1:
        if r == 0:

            return b
        a = b
        b = r
        r = a % b

a, b = map(int, input().split())

rst = uclide(a, b)
print('1' * rst)
