T=int(input())

for i in range(1,T+1):
    a = list(map(int,input().split(' ')))
    print('#'+str(i),round(sum(a)/10))
    
    