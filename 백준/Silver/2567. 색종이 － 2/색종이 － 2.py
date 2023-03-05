def put(y, x):
    for i in range(10):
        for j in range(10):
            paper[y + i][x + j] = 1


def check(a, b):
    cnt = 0
    for i in range(4):
        y = a + my[i]
        x = b + mx[i]

        if 0 > y or 0 > x or 100 <= y or 100 <= x:
            cnt += 1
            continue
        if paper[y][x] == 0:
            cnt += 1
    return cnt


n = int(input())
paper = [[0] * 100 for _ in range(100)]
my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]

for p in range(n):
    a, b = map(int, input().split())
    put(b, a)
ct = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            ct += check(i, j)


print(ct)
