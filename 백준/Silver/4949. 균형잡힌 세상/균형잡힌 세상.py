import sys

input = sys.stdin.readline

while 1:
    st = input().rstrip()
    if st == '.':
        break
    stack = [0]
    gwal = ['[', ']', '(', ')']
    for i in range(len(st)):
        if st[i] in gwal:
            if stack[-1] == '[' and st[i] == ']':
                stack.pop()
            elif stack[-1] == '(' and st[i] == ')':
                stack.pop()
            else:
                stack.append(st[i])

    if stack == [0]:
        print('yes')
    else:
        print('no')
