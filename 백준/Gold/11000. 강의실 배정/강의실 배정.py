import sys
import heapq

input = sys.stdin.readline

N = int(input())

time_lst = []
for i in range(N):
    a, b = map(int, input().split())
    time_lst.append((a, b))

# 시작시간으로 정렬
time_lst.sort(key= lambda x:x[0])
ans = []

for st, ed in time_lst:
    # 강의실 공유할때,
    if ans and ans[0] <= st:
        heapq.heappop(ans)
        heapq.heappush(ans, ed)
    #새로운 강의실 등록
    else:
        heapq.heappush(ans, ed)

print(len(ans))
