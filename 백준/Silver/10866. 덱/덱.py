import sys
from collections import deque

input = sys.stdin.readline
q = deque()
n = int(input())
for i in range(n):
    cmd = list(input().split())
    if len(cmd) == 2:
        if cmd[0] == 'push_back':
            q.append(cmd[1])
        else:
            q.appendleft(cmd[1])

    else:
        if q:
            if cmd[0] == 'pop_front':
                a = q.popleft()
                print(a)
            elif cmd[0] == 'pop_back':
                a = q.pop()
                print(a)
            elif cmd[0] == 'size':
                print(len(q))
            elif cmd[0] == 'empty':
                print(0)
            elif cmd[0] == 'front':
                print(q[0])
            else:
                print(q[-1])

        else:
            if cmd[0] == 'empty':
                print(1)
            elif cmd[0] == 'size':
                print(0)
            else:
                print(-1)

