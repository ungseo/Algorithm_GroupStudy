import sys

input = sys.stdin.readline

lst = [int(input()) for _ in range(3)]

gop = 1
for i in range(3):
    gop *= lst[i]

gop = str(gop)

for i in range(10):
    print(gop.count(str(i)))
