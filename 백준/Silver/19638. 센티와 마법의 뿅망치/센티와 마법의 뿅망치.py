import sys
import heapq
input = sys.stdin.readline

N, H, T = map(int, input().split())
H *= -1
giant = []
# 인풋
for i in range(N):
    heapq.heappush(giant, -int(input()))

flag = 1
# 때리기
for a in range(T):
    target = -heapq.heappop(giant)
    if -target > H:
        print("YES")
        print(a)
        flag = 0
        break
    target //= 2
    if target == 0:
        heapq.heappush(giant, -1)
    else:
        heapq.heappush(giant, -target)

    tallest = giant[0]
    if tallest > H:
        print("YES")
        print(a+1)
        flag = 0
        break

if flag:
    print('NO')
    print(-heapq.heappop(giant))



