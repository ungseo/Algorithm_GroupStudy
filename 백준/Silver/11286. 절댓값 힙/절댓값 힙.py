import sys, heapq

input = sys.stdin.readline

h = []
N = int(input())
for i in range(N):
    cmd = int(input())
    if cmd:
        if cmd > 0:
            x = cmd * 2
        else:
            x = cmd * (-2) - 1

        heapq.heappush(h, (x, cmd))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
