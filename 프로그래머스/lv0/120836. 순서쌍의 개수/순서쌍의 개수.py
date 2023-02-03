def solution(n):
    lst = []
    for i in range(1,n+1):
        if n % i == 0:
            lst.append(i)
    return len(lst)