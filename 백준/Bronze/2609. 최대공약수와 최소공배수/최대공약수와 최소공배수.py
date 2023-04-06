import sys

input = sys.stdin.readline

num = list(map(int, input().split()))
min = min(num)
max = max(num)

for i in range(min, 0, -1):
    if min % i == 0 and max % i == 0:
        print(i)
        break

for i in range(1,max+1):
    if (min * i) % max == 0:
        print(min * i)
        break
        