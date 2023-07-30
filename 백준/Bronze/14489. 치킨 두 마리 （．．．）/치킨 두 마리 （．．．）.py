A, B = map(int, input().split())
C = int(input())

tt = A + B
C *= 2

if tt >= C:
    print(tt-C)
else:
    print(tt)
