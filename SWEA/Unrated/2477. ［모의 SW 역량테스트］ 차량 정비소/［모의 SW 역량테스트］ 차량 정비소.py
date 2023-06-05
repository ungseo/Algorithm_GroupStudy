
T = int(input())

for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    Nt = list(map(int, input().split()))
    Mt = list(map(int, input().split()))
    Kt = list(map(int, input().split()))
    Nl = [0] * N
    Ml = [0] * M
    waitingN = []
    waitingM = []

    ans = []
    Ki  = 1
    time = 0
    flag = 2
    people = len(Kt)
    while 1:
        # 도착했니? 웨이팅룸에 넣어
        for i in range(len(Kt)):
            if Kt[i] == time:
                waitingN.append(Ki)
                Ki += 1
        waitingN.sort()
        # 접수창구 비어있니?? 기다리는 사람 집어넣어
        for i in range(len(Nl)):
            if Nl[i] == 0 and waitingN:
                customer = waitingN.pop(0)
                Nl[i] = [customer, Nt[i]]

        # 수리센터 비어있니?? 기다리는사람 집어넣어
        for i in range(len(Ml)):
            if Ml[i] == 0 and waitingM:
                customer = waitingM.pop(0)
                Ml[i] = customer + [Mt[i]]

        # 1초 흘렀어
        time += 1

        # 일하고 있는 창구 1초 감소시켜 0초인거는 사람빼서 M룸에 집어넣어
        temp = []
        for i in range(len(Nl)):
            if Nl[i] != 0:
                Nl[i][1] -= 1
                if Nl[i][1] == 0:
                    ed = Nl[i]
                    Nl[i] = 0
                    temp.append([ed[0], i + 1])  # 고객번호, 접수창구 번호
        temp.sort(key=lambda x: x[1])
        waitingM += temp


        # 일하고있는 수리센터 1초 감소시켜, 0초인거는 사람빼서 결과확인해
        for i in range(len(Ml)):
            if Ml[i] != 0:
                Ml[i][2] -= 1
                if Ml[i][2] == 0: # 어? 너나가
                    if Ml[i][1] == A and i+1 == B:
                        ans.append(Ml[i][0])

                    Ml[i] = 0
        if Ki - 1 == K:
            flag = 0
            for x in range(N):
                if Nl[x] != 0:
                    flag = 1
                    break
            for y in range(M):
                if Ml[y] != 0:
                    flag = 1
                    break
            if len(waitingN) or len(waitingM):
                flag = 1


        if not flag:
            break
    ans = sum(ans)

    if ans:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} -1')