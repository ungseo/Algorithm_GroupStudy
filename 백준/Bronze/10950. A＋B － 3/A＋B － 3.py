def hap(a, b):
    print(a + b)


T = int(input())

for tc in range(T):
    a, b = map(int, input().split())
    hap(a,b)