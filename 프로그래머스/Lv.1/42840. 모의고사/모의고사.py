def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5] * 8
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4

    check = [0, 0, 0]
    for i in range(len(answers)):
        idx = i % 40
        if answers[i] == first[idx]:
            check[0] += 1
        if answers[i] == second[idx]:
            check[1] += 1
        if answers[i] == third[idx]:
            check[2] += 1
    
    max_answer = max(check)
    
    for i in range(3):
        if check[i] == max_answer:
            answer.append(i+1)

    return answer