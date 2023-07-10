from collections import deque
import sys

input = sys.stdin.readline

def cmd1(string):
    return string[:-1]

def cmd2(string):
    return string[:-1][::-1]

S = input().rstrip()
T = input().rstrip()

t = len(T) - len(S)

for i in range(t):
    if T[-1] == 'A':
        T = cmd1(T)
    else:
        T = cmd2(T)

if T == S:
    print(1)
else:
    print(0)


