import sys

input = sys.stdin.readline


def uclid_two(a, b):
    r = a % b
    while 1:
        if r == 0:
            return b
        a = b
        b = r
        r = a % b



n, s = map(int, input().split())

numlst = list(map(int, input().split()))
numlst = list(map(lambda x: abs(x-s),numlst))
rst = numlst[0]
for i in range(len(numlst)):
    rst = uclid_two(rst, numlst[i])
print(rst)