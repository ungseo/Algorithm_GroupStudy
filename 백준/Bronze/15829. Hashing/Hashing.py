import sys
input = sys.stdin.readline

L = int(input())
st = input()
r = 31
M = 1234567891
hashsum = 0
for i in range(L):
    hashsum += (ord(st[i]) - 96) * r ** i
print(hashsum)

