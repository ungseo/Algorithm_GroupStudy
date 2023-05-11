import sys, heapq

input = sys.stdin.readline

h = []
N = int(input())
for i in range(N):
    cmd = int(input())

    if cmd:
        heapq.heappush(h, -cmd)
    else:
        if h:
            print(abs(heapq.heappop(h)))
        else:
            print(0)
