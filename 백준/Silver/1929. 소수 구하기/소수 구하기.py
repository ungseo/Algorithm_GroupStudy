import sys
input = sys.stdin.readline

m, n = map(int, input().split())
nlst = [1] * (n+1)

for i in range(2, n+1):
    if nlst[i]:
        if i >= m:
            print(i)
    for j in range(i+i, n+1, i):
        if j % i == 0:
            nlst[j] = 0


