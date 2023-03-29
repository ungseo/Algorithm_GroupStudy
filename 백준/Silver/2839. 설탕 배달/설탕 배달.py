import sys

input = sys.stdin.readline

n = int(input())

rst = 0
f = n % 5
flag = 0
for i in range(n // 5, -1, -1):
    f = n - (i * 5)
    if f % 3 == 0:
        rst += i + (f//3)
        flag = 1
        break
if flag == 0:
    rst = -1
print(rst)
