def solution(my_string):
    lst = my_string.split(' ')
    sum = int(lst[0])
    for i in range(1, len(lst)-1, 2):
        if lst[i] == '+':
            sum += int(lst[i+1])
        elif lst[i] == '-':
            sum -= int(lst[i+1])
            
    return sum