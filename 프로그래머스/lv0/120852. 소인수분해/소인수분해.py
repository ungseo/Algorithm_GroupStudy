def solution(n):
    DAT = [1] * (n+1)
    answer = []
    for i in range(2, n+1):
        if DAT[i] == 1:
            if n % i == 0:
                answer.append(i)
        for j in range(i+i, n+1, i):
            DAT[j] = 0

            
    return answer