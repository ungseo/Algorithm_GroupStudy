import sys
sys.setrecursionlimit(10**5)

def up(a, b):
    global num
    plus = -1
    while 1:
        if a + plus < 0 or seat[a + plus][b] > 0:
            if seat[a + plus + 1][b+1] > 0:
                return
            else:
                right(a + plus + 1, b)
                return
        else:
            seat[a + plus][b] = num
            plus -= 1
            num += 1


def down(a, b):
    global num
    plus = 1
    while 1:
        if a + plus >= y or seat[a + plus][b] > 0:
            if seat[a + plus - 1][b - 1] > 0:
                return
            else:
                left(a + plus - 1, b)
                return
        else:
            seat[a + plus][b] = num
            plus += 1
            num += 1


def left(a, b):
    global num
    plus = -1
    while 1:
        if b + plus < 0 or seat[a][b + plus] > 0:
            if seat[a-1][b + plus + 1] > 0:
                return
            else:
                up(a, b + plus + 1)
                return
        else:
            seat[a][b + plus] = num
            plus -= 1
            num += 1


def right(a, b):
    global num
    plus = 1
    while 1:
        if b + plus >= x or seat[a][b + plus] > 0:
            if seat[a+1][b + plus - 1] > 0:
                return
            else:

                down(a, b + plus - 1)
                return
        else:
            seat[a][b + plus] = num
            plus += 1
            num += 1


x, y = map(int, input().split())
k = int(input())
seat = [[0] * x for _ in range(y)]
movy = [-1, 0, 1, 0]
movx = [0, 1, 0, -1]
num = 2
seat[y - 1][0] = 1
up(y - 1, 0)
flag = 1
for i in range(y-1,-1,-1):
            for j in range(x):
                if seat[i][j] == k:
                    print(j+1,y-i)
                    flag = 0
                    break
            if flag == 0:break
if flag == 1:
    print(0)