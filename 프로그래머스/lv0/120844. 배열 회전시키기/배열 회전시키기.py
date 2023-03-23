def solution(numbers, direction):
    if direction == 'left':
        lst = numbers + [0]
        lst[0], lst[-1] = lst[-1], lst[0]
        answer = lst[1:]
    else:
        lst = [0] + numbers
        lst[0], lst[-1] = lst[-1], lst[0]
        answer = lst[:-1]
    return answer