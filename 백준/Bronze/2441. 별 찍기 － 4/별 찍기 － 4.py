n = int(input())

for j in range(n, 0, -1):
    print(' ' * (n-j) + '*' * j)
