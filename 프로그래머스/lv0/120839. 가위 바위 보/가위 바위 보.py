def solution(rsp):
    answer = ''
    rsp = list(map(int,map(str,rsp)))
    for i in range(len(rsp)):
        if rsp[i] == 2:
            answer += str(0)
        elif rsp[i] == 0:
            answer += str(5)
        else:
            answer += str(2)
    return answer
