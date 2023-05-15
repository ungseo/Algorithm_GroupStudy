mo = ['a','e','i','o','u']
def solution(my_string):
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] in mo:
                   my_string[i] = ''
    answer = ''.join(my_string)
        
    return answer