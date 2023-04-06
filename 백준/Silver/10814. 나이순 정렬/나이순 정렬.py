import sys

input = sys.stdin.readline

n = int(input())
member_lst = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    member_lst.append([age, name])

member_lst.sort(key=lambda x:x[0])

for i in member_lst:
    print(*i)