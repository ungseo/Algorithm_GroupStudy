def solution(emergency):
    copy_emergency = emergency[:]
    for j in range(1,len(copy_emergency)):   
        for i in range(len(copy_emergency)-j):
            if copy_emergency[i] < copy_emergency[i+1]:
                copy_emergency[i],copy_emergency[i+1] = copy_emergency[i+1],copy_emergency[i]
    
    rst = []
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if emergency[i] == copy_emergency[j]:
                rst.append(j+1)
                break
    return rst
                