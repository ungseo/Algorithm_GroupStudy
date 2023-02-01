'''
2023.02.01 알고리즘 스터디 문풀
'''

##### 13.피자 나눠 먹기(1)
def solution(n):
    pizza = 7
    if n % pizza !=0:
        answer = n//pizza+1
    else:
        answer = n//pizza
    return answer


##### 14.피자 나눠 먹기(2)
def solution(n):##pizza = 6조각,과 n의 최소공배수 구해야할듯?
    for i in range(max(6,n),6*n+1):
        if i % 6 == 0 and i % n == 0:
            lcd = i
            break
    
    return i // 6


##### 15.피자 나눠 먹기(3)
def solution(slice, n):
    if n % slice != 0:
        return n//slice + 1
    else:
        return n//slice


##### 16. 배열의 평균값
def solution(numbers):
    sum = 0
    
    for i in numbers:
        sum += i
    
    avg = sum/len(numbers)
    return avg


##### 17. 옷가게 할인 받기
def solution(price):
    if price >= 500000:
        sale = float(1/5)
    
    elif price >= 300000:
        sale = float(1/10)
    
    elif price >= 100000:
        sale = float(1/20)
    
    else:
        sale = 0
    
    return price*(1-sale)