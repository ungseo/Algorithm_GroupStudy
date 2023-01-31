##### 9. 나머지 구하기
def solution(num1, num2):
    answer = num1 % num2
    return answer

##### 10. 중앙값 구하기
def solution(array):
    array.sort()   #리스트 정렬
    
    if len(array) % 2 == 1:  ## 숫자개수가 홀수개면
        idx = (len(array)-1) // 2  ## 가운데 인덱스 뽑아서 출력
        answer = array[idx]
    
    else:
        idx1,idx2 = len(array)//2-1, len(array)//2 ## 숫자갯수가 짝수개면
        answer = (array[idx1]+array[idx2])/2       ## 가운데 두값 평균값 출력
    
    return answer



'''
다른사람의 풀이 중 이상한것
def solution(array):
    array = sorted(array)
    length = len(array)//2
    return array[length]
>> len(array)가 짝수면..? 중앙값의 의미가 맞는지??
'''

##### 11. 최빈값 구하기
def solution(array):
    from collections import Counter  ##Counter 모듈 불러오기
    cnt = dict(Counter(array))  ## 리스트 중복갯수 구하기
    Max = list(cnt.values())  ## 중복갯수 리스트로 만들기
    m = max(Max)            ## 제일많이 나온횟수 m에 지정
    Max.remove(m)           ## 중복횟수 리스트에서 m 삭제

    if m in Max:    ## 삭제했는데도 m이 남아있으면(최빈값이 2개이상이면)
        return -1  ## -1 리턴
    
    else:   ## m값이 2개이상이 아니면
        first = sorted(cnt.items(),key=lambda x:x[1],reverse=True)
        return first[0][0]  ## 중복 횟수 내림차순으로 정렬후 처음 key값 리턴

######################모듈안쓰고###########################

def solution(array):
    dic = {}
    for i in range(1000):   ## 제한사항내 모든 수 검사
        if array.count(i) != 0:  ## 없으면 스킵 있으면
            dic[i] = array.count(i) ## 딕셔너리에 갯수 추가
    
    dic = sorted(dic.items(),key=lambda x:-x[1])  ## 갯수 내림차순

    if len(dic) == 1:   
        return dic[0][0]
    elif dic[0][1] == dic[1][1]:
        return -1
    else:
        return dic[0][0]


##### 12. 짝수는 싫어요
def solution(n):

    answer = list(range(1,n+1,2))
    return answer

    
###############어제 7번문제 수정##############
def solution(numer1, denom1, numer2, denom2):
    for i in range(max(denom1,denom2),denom1*denom2+1,1):
        if i % denom1 == 0 and i % denom2 == 0:
            lcm = i
            break
    numer1 *= (lcm//denom1)
    numer2 *= (lcm//denom2)
    numer = numer1 + numer2
    
    for i in range(min(numer,lcm),0,-1):
        if numer % i == 0 and lcm % i == 0:
            gcd = i
            break

    return [numer//gcd,lcm//gcd]