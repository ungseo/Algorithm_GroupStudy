import sys

input = sys.stdin.readline

mlist = []  # 음수~ 0까지
plist = []  # 자연수
temp = []
ans = []
n = int(input())
for i in range(n):
    num = int(input())
    if num <= 0:
        mlist.append(num)
    else:
        plist.append(num)

mlist.sort()
plist.sort(reverse=True)

for i in range(0, len(mlist), 2):
    if i+1 == len(mlist):
        temp.append(mlist[i])
    else:
        rst1 = mlist[i] * mlist[i+1]
        rst2 = mlist[i] + mlist[i+1]
        if rst1 > rst2:
            ans.append(rst1)
        else:
            ans.append(rst2)

for i in range(0, len(plist), 2):
    if i+1 == len(plist):
        temp.append(plist[i])
    else:
        rst1 = plist[i] * plist[i+1]
        rst2 = plist[i] + plist[i+1]
        if rst1 > rst2:
            ans.append(rst1)
        else:
            ans.append(rst2)

if len(temp) == 1:
    ans.append(temp[0])
elif len(temp) == 2:
    ans.append(temp[0]+temp[1])

print(sum(ans))