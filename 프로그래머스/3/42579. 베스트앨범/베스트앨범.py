def solution(genres, plays):
    answer = []
    total = {}
    for i in range(len(genres)):
        if genres[i] in total:
            total[genres[i]][0] += plays[i]
            if len(total[genres[i]]) == 3: #꽉 비교
                
                if total[genres[i]][1][1] >= total[genres[i]][2][1]:
                    min_idx = 2
                else:
                    min_idx = 1
                if total[genres[i]][min_idx][1] < plays[i]:
                    total[genres[i]].pop(min_idx)
                    total[genres[i]].append((i, plays[i]))
                
            else: #하나만 차있으면
                total[genres[i]].append((i, plays[i]))
                
            
        else: #하나도 없으면
            total[genres[i]] = [plays[i], (i, plays[i])]

    sorted_dict = dict(sorted(total.items(), key = lambda x: x[1][0], reverse=True))
    
    
    for i in sorted_dict:
        if len(sorted_dict[i]) == 3:
            if sorted_dict[i][1][1] >= sorted_dict[i][2][1]:
                answer.append(sorted_dict[i][1][0])
                answer.append(sorted_dict[i][2][0])
            else:
                answer.append(sorted_dict[i][2][0])
                answer.append(sorted_dict[i][1][0])
        else:
            answer.append(sorted_dict[i][1][0])

            
                
    
    
    return answer