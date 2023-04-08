import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    F = int(input())
    ho = int(input())
    apt = list(range(1,ho+1))
    if F == 0:
        print(apt[ho-1])
    else:
        for f in range(F):
            for h in range(1,ho):
                apt[h] += apt[h-1]
        print(apt[ho-1])


