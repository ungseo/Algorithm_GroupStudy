def blackpp(y,x):
    for i in range(10):
        for j in range(10):
            paper[y+i][x+j] += 1
        


n = int(input())
paper = [[0] * 100 for i in range(100)]
ans = 0

for _ in range(1,n+1):
    py, px = map(int,input().split())
    blackpp(90-py,px)

for ea in range(1,n+1):    
    for i in range(100):
        for j in range(100):
            if paper[i][j] != 0 and paper[i][j] == ea:
                ans += paper[i][j]//ea

print(ans)
