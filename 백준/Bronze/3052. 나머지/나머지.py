import sys
input = sys.stdin.readline

lst = []
for i in range(10):
    n = int(input())

    rst = n % 42
    if rst not in lst:
        lst.append(rst)
print(len(lst))
