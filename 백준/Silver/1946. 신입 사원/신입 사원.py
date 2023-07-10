import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = map(int, input().split())
        lst.append((a, b))

    lst.sort()
    cnt = 1
    best_interview_rank = lst[0][1]
    for i in range(1, len(lst)):
        if lst[i][1] < best_interview_rank:
            cnt += 1
            best_interview_rank = lst[i][1]

    print(cnt)

