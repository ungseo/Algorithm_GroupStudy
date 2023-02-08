n= int(input())
lst = list(map(int,input().split()))

M = 0 
for i in lst:
    if M < i:
        M = i
temp = []
for i in lst:
    temp.append(i/M*100)
sum = 0
for i in temp:
    sum += i

print(sum/len(temp))
