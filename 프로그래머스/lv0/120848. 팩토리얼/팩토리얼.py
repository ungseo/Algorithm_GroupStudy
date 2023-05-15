def factorial(x):
    if x == 1: 
        return x
    return x * factorial(x-1)



def solution(n):
    for i in range(10, 0, -1):
        rst = factorial(i)
        if rst <= n:
            answer = i
            return answer
    
    