##### 21.문자열 뒤집기
def solution(my_string):
    answer = my_string[::-1]
    return answer

##### 22. 직각삼각형 출력하기
n = int(input())
for i in range(1,n+1):
    print('*'*i)

##### 23. 짝수 홀수 개수
def solution(num_list):
    odd = 0
    even = 0
    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd +=1
    return [even,odd]

##### 24. 문자 반복 출력하기
def solution(my_string, n):
    string =''
    for i in my_string:
        string += i*n

    return string

##### 25. 특정 문자 제거하기
def solution(my_string, letter):
    temp = []
    for i in list(my_string):
        if i == letter:
            pass
        else:
            temp.append(i)
    
    return ''.join(temp)

'''
continue와
pass의 차이점..?
뭘 써도 상관없는거같은데..?
'''

##### 26. 각도기
def solution(angle):
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle < 180:
        return 3
    elif angle == 180:
        return 4


##### 27. 양꼬치
def solution(n, k):
    service = n // 10
    return 12000 * n + (k - service) * 2000

print(solution(20,0))  ## 236000


def solution(n, k):
    service = n//10
    drink = max(0, k-service) ##꼭 필요한 조건
    return (12000*n)+(2000*drink)
    ###수정


##### 28.짝수의 합
def solution(n):
    rst = 0
    for i in range(0,n+1,2):
        rst += i
    return rst

##### 29. 옹알이
def solution(babbling):
    for i in babbling:
        list().pop( )