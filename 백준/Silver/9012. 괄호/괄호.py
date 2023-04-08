import sys

input = sys.stdin.readline

T = int(input().rstrip())
for tc in range(T):
    stack = [0]
    gwal = list(input().rstrip())
    for i in range(len(gwal)):
        if stack[-1] == '(':
            if gwal[i] == ')':
                stack.pop()
            else:
                stack.append('(')
        else:
            stack.append(gwal[i])
    if stack == [0]:
        print('YES')
    else:
        print('NO')
