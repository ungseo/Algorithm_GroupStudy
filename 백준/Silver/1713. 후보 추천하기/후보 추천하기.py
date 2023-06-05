import sys

input = sys.stdin.readline

N = int(input())
TR = int(input())
recommendation = list(map(int, input().split()))  ## input

frame = [] # 액자 리스트
number = [0] * 101 # 학생 추천 받은 수 bucket 배열

for i in range(TR):
    # 액자가 빈 곳이 있을때
    if len(frame) < N:
        number[recommendation[i]] += 1
        # 추천 받은 애가 또 추천 받았을 때
        if number[recommendation[i]] > 1:
            for j in range(len(frame)):
                if frame[j][2] == recommendation[i]: # 추천받은 애 찾아서 갱신 후 sort
                    frame[j][0] += 1
                    frame.sort(key=lambda x: (x[0], x[1]))
                    break
        # 새로운 학생이 추천 받았을 때
        else: #빈 곳에 넣고 sort
            frame.append([number[recommendation[i]], i + 1, recommendation[i]])  # 횟수, 순서, 학생번호
            frame.sort(key=lambda x: (x[0], x[1]))

    # 액자가 꽉찬 상태에서 갱신해야 할 때
    else:
        number[recommendation[i]] += 1
        # 액자에 있는 학생이 추천 받았을 때
        if number[recommendation[i]] > 1:
            for j in range(len(frame)):  # 학생 찾아서 갱신 후 sort
                if frame[j][2] == recommendation[i]:
                    frame[j][0] += 1
                    frame.sort(key=lambda x: (x[0], x[1]))
                    break

        # 새로운 애가 추천 받았는데 액자가 꽉찬 상황
        else:
            number[frame[0][2]] = 0 # 액자의 맨앞(0번인덱스)은 제거대상 1위이므로 맨앞 학생의 추천수를 0으로 초기화
            frame[0] = [number[recommendation[i]], i + 1, recommendation[i]] # 액자 맨앞을 새로 추천받은 학생으로 갱신
            frame.sort(key=lambda x: (x[0], x[1])) # 제거대상 1순위를 위해 sort


# 모든 작업 끝난 후 답 출력을 위해 액자 학생번호 순으로 sort 후 출력.
frame.sort(key=lambda x:x[2])
for i in range(len(frame)):
    print(frame[i][2], end=' ')
