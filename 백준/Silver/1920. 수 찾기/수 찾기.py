import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
checklst = list(map(int, input().split()))


for i in range(m):
    st = 0
    ed = len(lst) - 1
    mid = (st + ed) // 2
    flag = 0
    while st <= ed:

        if lst[mid] == checklst[i]:
            flag = 1
            break
        elif lst[mid] > checklst[i]:
            ed = mid - 1
            mid = (st + ed) // 2
        else:
            st = mid + 1
            mid = (st + ed) // 2
    print(flag)
