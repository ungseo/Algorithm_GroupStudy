def solution(dot):
    x = dot[0]
    y = dot[1]
    if x < 0:
        if y < 0:
            answer = 3
        else:
            answer = 2
    else:
        if y < 0:
            answer = 4
        else:
            answer = 1
        
    return answer