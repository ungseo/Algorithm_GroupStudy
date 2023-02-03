def solution(hp):
    cnt = 0
    while hp != 0:
        if hp >= 5:
           cnt += hp//5
           hp = hp % 5
        elif hp >= 3:
            cnt += hp//3 
            hp = hp % 3
        else:
            cnt += hp
            hp = 0
    return cnt