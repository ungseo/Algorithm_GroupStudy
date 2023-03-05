def put(y,x,w,h,seq):
    for i in range(h):
        for j in range(w):
            paper[y+i][x+j] = seq

paper = [[0]*1001 for _ in range(1001)]
n = int(input())
for p in range(1,n+1):
    x, y, w, h = map(int,input().split())
    put(y,x,w,h,p)


for num in range(1,n+1):
    rst = 0
    for i in range(1001):
        for j in range(1001):
            if paper[i][j] == num:
                rst += 1
    print(rst)