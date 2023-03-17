import sys

input = sys.stdin.readline

lst = []
for i in range(28):
    lst.append(int(input()))
lst.sort()
vslst = list(range(1, 31))

for i in range(30):
    if vslst[i] not in lst:
        print(vslst[i])