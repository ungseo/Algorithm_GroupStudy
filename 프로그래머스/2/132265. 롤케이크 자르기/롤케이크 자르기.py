def solution(topping):
    topping_list = [0] * 10001
    topping_cnt = 0
    answer = 0
    
    for i in topping:
        if topping_list[i] == 0:
            topping_cnt += 1    
        topping_list[i] += 1
        
    bro_cake = []
    bro_topping = 0
    bro_toppinglst = [0] * 10001

    while topping:
        cut = topping.pop()
        topping_list[cut] -= 1
        bro_toppinglst[cut] += 1
        if bro_toppinglst[cut] == 1:
            bro_topping += 1
        if topping_list[cut] == 0:
            topping_cnt -= 1
        if bro_topping == topping_cnt:
            answer += 1
            
    
    return answer