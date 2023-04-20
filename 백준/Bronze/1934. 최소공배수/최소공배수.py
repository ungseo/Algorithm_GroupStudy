import sys

input = sys.stdin.readline

def uclide(a, b):
    # a = max(a, b)
    # b = min(a, b)
    r = a % b
    while 1:
        if r == 0:
            return b
        a = b
        b = r
        r = a % b

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    GCD = uclide(a, b)
    ans = a * b // GCD
    print(ans)