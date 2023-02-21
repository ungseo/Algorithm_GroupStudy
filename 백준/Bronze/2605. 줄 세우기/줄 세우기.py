stduents = int(input())
num_lst = list(map(int,input().split()))
rst_lst = []

for i in range(1,stduents+1):
    if num_lst[i-1] == 0:
        rst_lst.append(i)
    else:
        rst_lst.insert(i-num_lst[i-1]-1,i)

print(*rst_lst)
