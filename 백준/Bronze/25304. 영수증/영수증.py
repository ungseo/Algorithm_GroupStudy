Total = int(input())

ea = int(input())
sum = 0
for i in range(ea):
    product, price = map(int,input().split())
    sum += product * price

if sum == Total:
    print('Yes')
else:
    print('No')
   