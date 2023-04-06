import heapq, sys

input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n):
    heapq.heappush(heap, int(input()))
sum = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum += a + b
    heapq.heappush(heap, a + b)

print(sum)

