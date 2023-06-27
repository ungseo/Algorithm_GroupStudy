import sys

input = sys.stdin.readline

Y, X = map(int, input().split())
castle = [list(input().rstrip()) for _ in range(Y)]
y = []
x = []
for i in range(Y):
    rst = castle[i].count('X')
    if rst:
        pass
    else:
        y.append(i)
for i in range(X):
    cnt = 0
    for j in range(Y):
        if castle[j][i] == 'X':
            cnt += 1
    if cnt:
        pass
    else:
        x.append(i)
a = len(y)
b = len(x)

print(max(a,b))

