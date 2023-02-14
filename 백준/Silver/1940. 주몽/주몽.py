N = int(input())
M = int(input())

lst = list(map(int,input().split()))

lst.sort()

sp = 0
ed = 1
cnt = 0

while sp != len(lst)-1:
    sum = lst[sp] + lst[ed]
    ed += 1
    if sum == M:
        cnt +=1
    sum = 0
    if ed == len(lst):
        sp += 1
        ed = sp +1
    
print(cnt)
    