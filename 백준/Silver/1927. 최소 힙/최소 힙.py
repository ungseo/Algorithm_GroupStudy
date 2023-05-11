import sys
import heapq
input = sys.stdin.readline

N = int(input())
h = []

for i in range(N):
    cmd = int(input())
    if cmd == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h,cmd)
