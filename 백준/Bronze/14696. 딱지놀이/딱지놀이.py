def vs(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

n = int(input())

for round in range(n):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    star_A, circle_A, square_A, triangle_A = 0, 0, 0, 0
    star_B, circle_B, square_B, triangle_B = 0, 0, 0, 0

    for i in A[1:]:
        if i == 4:
            star_A += 1
        elif i == 3:
            circle_A += 1
        elif i == 2:
            square_A += 1
        else:
            triangle_A += 1
    for i in B[1:]:
        if i == 4:
            star_B += 1
        elif i == 3:
            circle_B += 1
        elif i == 2:
            square_B += 1
        else:
            triangle_B += 1
    lstA = [star_A, circle_A, square_A, triangle_A]
    lstB = [star_B, circle_B, square_B, triangle_B]

    draw_cnt = 0
    for game in range(4):
        rst = vs(lstA[game],lstB[game])
        if rst == 1:
            print('A')
            break
        elif rst == -1:
            print('B')
            break
        else:
            draw_cnt += 1
    if draw_cnt == 4:
        print('D')



