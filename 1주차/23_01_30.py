##### 1. 두수의 합

def solution(num1, num2):
    answer = num1 + num2
    return answer

##### 2. 두수의 차
def solution(num1, num2):
    answer = num1 - num2
    return answer

##### 3. 두수의 곱
def solution(num1, num2):
    answer = num1 * num2
    return answer

##### 4. 몫 구하기
def solution(num1, num2):
    answer = num1 // num2
    return answer

##### 5. 두 수의 나눗셈
def solution(num1, num2):
    answer = (num1 / num2) * 1000
    return int(answer)

##### 6. 숫자 비교하기
def solution(num1, num2):
    flag = num1 == num2
    if flag:
        return 1
    else:
        return -1

##### 7. 분수의 덧셈
def solution(numer1, denom1, numer2, denom2):
    import math
    
    lcm = math.lcm(denom1,denom2)
    numer1 *= int(lcm/denom1) 
    numer2 *= int(lcm/denom2)
    return [numer1+numer2,lcm]

def solution(numer1, denom1, numer2, denom2):
    for i in range(max(denom1,denom2),denom1*denom2+1,1):
        if i % denom1 == 0 and i % denom2 == 0:
            lcm = i
            break
    numer1 *= (int(lcm/denom1))
    numer2 *= (int(lcm/denom2))
    numer1,numer2 = int(numer1),int(numer2)
    return [numer1+numer2,lcm]

print(solution(12,2,3,7))

##### 8. 배열 두배 만들기
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    
    return answer

##### 9. 나머지 구하기
def solution(num1, num2):
    answer = num1 % num2
    return answer