def solution(sizes):
    max_garo = 0
    max_sero = 0
    
    for i in sizes:
        garo, sero = max(i[0], i[1]), min(i[0], i[1])
        if garo > max_garo:
            max_garo = garo
        if sero > max_sero:
            max_sero = sero

    
    answer = max_garo * max_sero
    
    
    return answer