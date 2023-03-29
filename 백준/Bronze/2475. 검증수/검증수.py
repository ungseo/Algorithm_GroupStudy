import sys

input = sys.stdin.readline

check_num = list(map(int, input().split()))

sum = 0
for i in range(5):
    sum += check_num[i] ** 2

rst = sum % 10

print(rst)