def batch(dir,dis,num):
    if dir == 1:
        north[dis-1] = num
    elif dir == 2:
        south[dis] = num
    elif dir == 3:
        west[dis] = num
    else:
        east[dis-1] = num

garo, sero = map(int,input().split())
north = [0] * garo
south = [0] * garo
west = [0] * sero
east = [0] * sero

n = int(input())
for i in range(1,n+2):
    direction, distance = map(int,input().split())
    batch(direction, distance, i)

line = north + east + south[::-1] + west[::-1]

for i in range(len(line)):
    if line[i] == n+1:
        st_idx = i
        break
rst = 0
for i in range(1,n+1):
    pointer = st_idx
    cnt = 0
    while 1:
        if pointer == len(line)-1:
            pointer = 0
            cnt += 1
        if line[pointer] == i:
            break
        else:
            pointer += 1
            cnt += 1

    if cnt > garo + sero:
        rst += (garo+sero)*2 - cnt
    else:
        rst += cnt

print(rst)