n, k = map(int, input().split())
a = n
b = k
c = k
if k == 0:
    print(1)
else:
    for i in range(k-1):
        n -= 1
        a *= n
        c -= 1
        b *= c
    
    print(a//b)
