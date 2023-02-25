x, y = map(int,input().split())

cut = int(input())
garo = []
sero = []
wide = []
height = []
for c in range(cut):
    direction, point = map(int, input().split())
    if direction == 0:
        garo.append((direction, point))
    else:
        sero.append((direction, point))

sero.sort(key= lambda x: x[1])
garo.sort(key= lambda x: x[1])
start = 0
if len(sero) >= 1:
    for w in range(len(sero)):
        wide.append(sero[w][1] - start)
        start = sero[w][1]
    wide.append(x-sero[len(sero)-1][1])
else:
    wide.append(x)
start = 0
if len(garo) >= 1:
    for h in range(len(garo)):
        height.append(garo[h][1] - start)
        start = garo[h][1]
    height.append(y-garo[len(garo)-1][1])
else:
    height.append(y)

print(max(height)*max(wide))