import sys

input = sys.stdin.readline

n, m = map(int,input().split())

top = 1
bottom = 1
for i in range(m):
    top *= (n-i)
    bottom *= (m-i)

print(top//bottom)