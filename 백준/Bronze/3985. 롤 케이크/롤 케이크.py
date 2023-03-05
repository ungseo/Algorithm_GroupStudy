def cutting(a, b, seq):
    for i in range(a, b + 1):
        if roll_cake[i] == 0:
            roll_cake[i] = seq


L = int(input())
n = int(input())
roll_cake = [0] * (L + 1)
expect = []

maxS = 0
maxi = 0
for l in range(1, n + 1):
    p, k = map(int, input().split())
    if k - p > maxS:
        maxS = k - p
        maxi = l
    cutting(p, k, l)

maxP = 0
maxI = 0
for i in range(1, n + 1):
    if roll_cake.count(i) > maxP:
        maxP = roll_cake.count(i)
        maxI = i

print(maxi)
print(maxI)
