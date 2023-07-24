import sys

input = sys.stdin.readline

n, m = map(int,input().split())

min_mileage = [0] * n

for i in range(n):
    p, l = map(int,input().split())
    mileage = list(map(int,input().split()))
    
    if len(mileage) < l:
        min_mileage[i] = 1
        continue
    
    mileage.sort(reverse=True)
    min_mileage[i] = mileage[l-1]
    
hap = 0
min_mileage.sort()
flag = 1
for i in range(n):
    hap += min_mileage[i]
    if hap > m:
        flag = 0
        print(i)
        break
    elif hap == m:
        flag = 0 
        print(i+1)
        break
if flag:
    print(n)