n = int(input())
dice_lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    dice_lst[i][5], dice_lst[i][1] = dice_lst[i][1], dice_lst[i][5]
    dice_lst[i][3], dice_lst[i][4] = dice_lst[i][4], dice_lst[i][3]

maxSum = 0
for st in range(6):
    temp = dice_lst[0][:]
    stack = []
    if st % 2 == 0:
        stack.append(temp.pop(st))
        stack.append(temp.pop(st))
    else:
        stack.append(temp.pop(st))
        stack.append(temp.pop(st-1))
    sum = max(temp)
    for i in range(1, n):
        temp = dice_lst[i][:]
        for j in range(0, 6, 2):
            if temp[j] == stack[-1]:
                stack.append(temp.pop(j))
                stack.append(temp.pop(j))
                sum += max(temp)
                break
            elif temp[j+1] == stack[-1]:
                stack.append(temp.pop(j+1))
                stack.append(temp.pop(j))
                sum += max(temp)
                break
        if maxSum < sum:
            maxSum = sum
print(maxSum)