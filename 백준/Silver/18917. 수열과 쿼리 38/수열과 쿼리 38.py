import sys

input = sys.stdin.readline

M = int(input())
sum = 0
xor = 0
for query in range(M):
    cmdL = list(map(int, input().split()))
    if len(cmdL) == 1:
        if cmdL[0] == 3:
            print(sum)
        else:
            print(xor)
    else:
        cmd, value = cmdL[0], cmdL[1]
        if cmd == 1:
            sum += value
            xor ^= value
        else:
            sum -= value
            xor ^= value