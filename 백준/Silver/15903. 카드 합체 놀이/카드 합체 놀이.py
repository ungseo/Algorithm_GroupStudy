import sys
import heapq



input = sys.stdin.readline

n, m = map(int, input().split())

card = list(map(int, input().split()))
heapq.heapify(card)

for i in range(m):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    rst = a + b
    heapq.heappush(card, rst)
    heapq.heappush(card, rst)

print(sum(card))