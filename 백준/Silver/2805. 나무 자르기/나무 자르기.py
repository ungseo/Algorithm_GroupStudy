import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree_height = list(map(int, input().split()))
tree_height.sort()

st = 0
ed = tree_height[-1]
saw = (st + ed) // 2
ans = []
flag = 0
while st <= ed:
    my_tree = 0
    for i in range(n):
        if tree_height[i] > saw:
            my_tree += tree_height[i] - saw

    if my_tree == m:
        flag = 1
        print(saw)
        break

    elif my_tree > m:
        ans.append((saw, my_tree-m))
        st = saw + 1
        saw = (st + ed) // 2

    else:
        ed = saw - 1
        saw = (st + ed) // 2

if flag == 0 :
    ans.sort(key=lambda x:x[1])
    print(ans[0][0])
