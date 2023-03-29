def check(y, x):
    edit_cnt1 = 0
    for i in range(8):
        for j in range(8):
            if (y + i) % 2 == 1 and (x + j) % 2 == 1:
                if chess[y + i][x + j] == 'B':
                    edit_cnt1 += 1
            elif (y + i) % 2 == 1 and (x + j) % 2 == 0:
                if chess[y + i][x + j] == 'W':
                    edit_cnt1 += 1
            elif (y + i) % 2 == 0 and (x + j) % 2 == 0:
                if chess[y + i][x + j] == 'B':
                    edit_cnt1 += 1
            elif (y + i) % 2 == 0 and (x + j) % 2 == 1:
                if chess[y + i][x + j] == 'W':
                    edit_cnt1 += 1
    edit_cnt2 = 0
    for i in range(8):
        for j in range(8):
            if (y + i) % 2 == 1 and (x + j) % 2 == 1:
                if chess[y + i][x + j] == 'W':
                    edit_cnt2 += 1
            elif (y + i) % 2 == 1 and (x + j) % 2 == 0:
                if chess[y + i][x + j] == 'B':
                    edit_cnt2 += 1
            elif (y + i) % 2 == 0 and (x + j) % 2 == 0:
                if chess[y + i][x + j] == 'W':
                    edit_cnt2 += 1
            elif (y + i) % 2 == 0 and (x + j) % 2 == 1:
                if chess[y + i][x + j] == 'B':
                    edit_cnt2 += 1

    if edit_cnt1 > edit_cnt2:
        return edit_cnt1
    else:
        return edit_cnt2


n, m = map(int, input().split())
chess = [list(input()) for _ in range(n)]

minV = 21e8
for i in range(0, n - 7):
    for j in range(0, m - 7):
        rst = 64 - check(i, j)
        if minV > rst:
            minV = rst

print(minV)
