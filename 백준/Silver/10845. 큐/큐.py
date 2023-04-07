import sys

input =sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if stack:
            a = stack.pop(0)
            print(a)
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
