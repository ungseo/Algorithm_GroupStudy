Map = [[0]*101 for i in range(101)]


for i in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            Map[y][x] = 1

rst = 0
for i in range(101):
    for j in range(101):
        if Map[i][j] == 1:
            rst += 1

print(rst)