import sys

input = sys.stdin.readline

M = int(input())
S = list()

for i in range(M):
    cmd = input().rstrip()
    if cmd !='all' and cmd!='empty':
        cmd, value = cmd.split(' ')

    if cmd[1] == 'd' and value not in S:
        S.append(value)
    elif cmd[1] == 'e' and value in S:
        S.remove(value)
    elif cmd[1] == 'h':
        if value in S:
            print(1)
        else:
            print(0)
    elif cmd[1] == 'o':
        if value in S:
            S.remove(value)
        else:
            S.append(value)
    elif cmd[1] == 'l':
        S = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
             '20']
    else:
        S = []
