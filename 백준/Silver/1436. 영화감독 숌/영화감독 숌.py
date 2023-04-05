import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
stn = 666
while 1:
    if n == cnt:
        print(stn)
        break
    stn += 1
    if '666' in str(stn):
        cnt += 1

