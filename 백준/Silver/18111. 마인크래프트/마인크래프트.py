import sys
input = sys.stdin.readline

N, M, b = map(int, input().split())

floor = []
for _ in range(N):
    floor += list(map(int, input().split()))
minT = 21e8
minH = 0

for h in range(257):
    flag = 1
    time = 0
    B = b

    for i in range(N*M):
        if floor[i] == h: continue
        # 낮을때 인벤토리 블록 꺼내서 놓기
        if floor[i] < h:
            B -= (h-floor[i])
            time += (h - floor[i])
        #높을때 땅파서 인벤채우기
        else:
            work = floor[i] - h
            time += work * 2
            B += work

    if B < 0:
        flag = 0
    if flag == 1 and minT >= time:
        minT = time
        minH = h


print(minT, minH)
