n, k = map(int,input().split())
temper = list(map(int,input().split()))

rst = 0
for i in range(k):
    rst += temper[i]
maxT = rst
for i in range(n-k):
    rst -= temper[i]
    rst += temper[i+k]
    if maxT < rst:
        maxT = rst
print(maxT)