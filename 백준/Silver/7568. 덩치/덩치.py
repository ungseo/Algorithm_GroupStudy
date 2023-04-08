import sys

input = sys.stdin.readline

n = int(input())
people = []
d_grade = [1] * n
for i in range(n):
    w, h = map(int, input().split())
    people.append((w, h))

for i in range(n-1):
    for j in range(i+1, n):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            d_grade[j] += 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            d_grade[i] += 1

for i in range(n):
    print(d_grade[i],end=' ')

