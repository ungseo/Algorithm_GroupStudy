import sys

T = int(sys.stdin.readline())
for tc in range(1, 1 + T):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{tc}: {a + b}')
