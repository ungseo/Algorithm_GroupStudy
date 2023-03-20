def solution(balls, share):
    # 분자구하기
    t = balls
    n = balls
    for i in range(share-1):
        t *= (n-1)
        n -= 1
    # 분모 구하기
    d = 1
    for i in range(1,share+1):
        d *= i
    return t//d