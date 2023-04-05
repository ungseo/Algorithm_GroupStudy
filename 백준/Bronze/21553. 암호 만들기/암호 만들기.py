import sys
input = sys.stdin.readline

A = input().rstrip()
P = input().rstrip()

B = ''
for i in list('123456789'):
    if i in A: continue
    else:
        B += i
        break
B += P

for i in list('123456789'):
    if i in A: continue
    else:
        B += i
        break

print(B)