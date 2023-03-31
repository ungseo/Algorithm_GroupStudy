import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

# 부분합 계산
prefix_sum = [0]
for i in range(n):
    prefix_sum.append(prefix_sum[-1] + lst[i])

for i in range(m):
    a, b = map(int, input().split())
    # 부분합을 이용해 구간 합 계산
    print(prefix_sum[b] - prefix_sum[a-1])
