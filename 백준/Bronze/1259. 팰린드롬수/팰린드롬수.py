import sys

input = sys.stdin.readline

while 1:
    st = input().rstrip()
    if st == '0':
        break
    if st == st[::-1]:
        print('yes')
    else:
        print('no')

