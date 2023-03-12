import sys
n = int(sys.stdin.readline())
for tc in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{tc}: {a} + {b} = {a + b}')
