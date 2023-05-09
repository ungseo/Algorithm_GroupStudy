T = int(input())

for i in range(T):
    st = input()
    if len(st) == 1:
        print(st[0]+st[0])
    else:
        print(st[0]+st[-1])