import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    H, W, N = map(int, input().split())
    cnt = 0
    flag = 0
    for ho in range(1, W + 1):
        for F in range(1, H + 1):
            cnt += 1
            if cnt == N:
                print(F, end='')
                if ho < 10:
                    print('0' + str(ho))
                else:
                    print(ho)
                flag = 1
                break
        if flag == 1:
            break