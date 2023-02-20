cheolsu = [list(map(int,input().split())) for _ in range(5)]
host = [list(map(int,input().split())) for _ in range(5)]
host1 = host[0] + host[1] + host[2] + host[3] + host[4]
flag = 1
line_bingo = 0
time = 0
for num in host1:
    for i in range(5):
        for j in range(5):
            X_bingo = 0
            if cheolsu[i][j] == num:
                cheolsu[i][j] = 'X'
                time += 1
                if cheolsu[i] == ['X','X','X','X','X']:
                    line_bingo += 1
                cnt = 0
                for v in range(5):
                    if cheolsu[v][j] == 'X':
                        cnt += 1
                if cnt == 5:
                    line_bingo += 1

                if cheolsu[2][2] == 'X':
                    cnt = 0
                    for i in range(5):
                        if cheolsu[i][i] == 'X':
                           cnt += 1
                    if cnt == 5:
                        X_bingo += 1
                    cnt = 0
                    for i in range(4,-1,-1):
                        if cheolsu[i][4-i] == 'X':
                            cnt += 1
                    if cnt == 5:
                        X_bingo += 1
            if line_bingo + X_bingo >= 3:
                flag = 0
                print(time)
                break
        if not flag:
            break
    if not flag:
        break
