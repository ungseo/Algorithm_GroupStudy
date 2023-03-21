def solution(num_list, n):
    l = len(num_list)
    answer = []
    idx = -1
    while 1:
        temp = []
        for i in range(n):
            idx += 1
            temp.append(num_list[idx])
        answer.append(temp)
        
        if idx == l-1:
            break
        
    return answer