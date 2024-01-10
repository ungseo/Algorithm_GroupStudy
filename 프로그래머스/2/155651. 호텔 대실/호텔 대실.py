def solution(book_time):
    answer = 0
    bt = []
    for i in book_time:
        Sh, Sm = map(int, i[0].split(":"))
        Eh, Em = map(int, i[1].split(":"))
        
        St = Sh * 60 + Sm
        Et = Eh * 60 + Em
        
        bt.append([St, Et + 10])
    bt.sort(key = lambda x:x[1])
    
    room = [bt[0][1]]
    cnt = 1
    for i in range(1, len(bt)):
        min_HT = 21e8
        min_idx = 9999
        for j in range(len(room)):
            if bt[i][0] >= room[j] and min_HT > (bt[i][0] - room[j]):
                min_HT = bt[i][0] - room[j]
                
                min_idx = j
        if min_HT == 21e8 and min_idx == 9999:
            room.append(bt[i][1])
            cnt += 1
        else:
            room[min_idx] = bt[i][1]
    return cnt



