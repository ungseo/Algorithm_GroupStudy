def solution(numbers, k):
    if k == 1:
        answer = numbers[0]
    
    else:
        idx = 2 * (k-1) % len(numbers) 
        answer = numbers[idx]
    
    return answer