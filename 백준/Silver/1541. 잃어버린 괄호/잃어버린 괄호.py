import sys

input = sys.stdin.readline

sik = input().rstrip()

nl = []
num = ''
for i in range(len(sik)):
    if 48 <= ord(sik[i]) <= 57:
        num += sik[i]
    else:
        nl.append(int(num))
        num = ''
        nl.append(sik[i])

nl.append(num)
if len(nl) == 1:
    print(nl[0])

else:

    ans = []
    sum = 0
    for i in range(1, len(nl), 2):
        sum += nl[i-1]
        if nl[i] == '-':
            ans.append(sum)
            sum = 0
    if nl[-2] == '-':
        ans.append(int(nl[-1]))
    else:
        sum += int(nl[-1])
        ans.append(sum)
    rst = ans[0]
    for i in ans[1:]:
        rst -= i
    print(rst)