tall_lst = []
for cm in range(9):
    tall_lst.append(int(input()))

nine_cm = sum(tall_lst)
flag = 1
cha = 0
for f in range(8):
    cha += tall_lst[f]
    for s in range(f+1,9):
        cha += tall_lst[s]
        if nine_cm - cha == 100:
            tall_lst[f] = 0
            tall_lst[s] = 0
            flag = 0
            break
        cha -= tall_lst[s]
    cha -= tall_lst[f]
    if flag == 0:
        break

tall_lst.sort()

for i in range(9):
    if tall_lst[i] > 0:
        print(tall_lst[i])