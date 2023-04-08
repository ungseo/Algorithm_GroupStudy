import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    p = list(input().rstrip())
    n = int(input())
    lst = input().rstrip()
    dir = 1
    # 홀수이면 정방향, 짝수이면 역방향
    if len(lst) == 2:
        st = []
    else:
        st = deque(list(map(str, lst[1:len(lst) - 1].split(','))))
    if p.count('D') > n:
        print('error')
    else:
        flag = 1

        for i in range(len(p)):
            if p[i] == 'R':
                dir += 1
            else:
                if st:
                    if dir % 2 == 0:
                        st.pop()
                    else:
                        st.popleft()

                else:
                    flag = 0
                    break
        if dir % 2 == 0:
            st = list(st)[::-1]

        if flag == 1:
            rst = '[' + ','.join(st) + ']'
            print(rst)
        else:
            print('error')