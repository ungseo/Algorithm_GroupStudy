n, k = map(int,input().split())

g1b, g1g, g2b, g2g, g3b, g3g = 0, 0 ,0, 0, 0, 0
g4b, g4g, g5b, g5g, g6b, g6g = 0, 0, 0, 0, 0, 0
for _ in range(n):
    s, y = map(int,input().split())
    if s:
        if y == 1:
            g1b += 1
        elif y == 2:
            g2b += 1
        elif y == 3:
            g3b += 1
        elif y == 4:
            g4b += 1
        elif y == 5:
            g5b += 1
        else:
            g6b += 1
    else:
        if y == 1:
            g1g += 1
        elif y == 2:
            g2g += 1
        elif y == 3:
            g3g += 1
        elif y == 4:
            g4g += 1
        elif y == 5:
            g5g += 1
        else:
            g6g += 1
room = 0

for i in [g1b, g1g, g2b, g2g, g3b, g3g, g4b, g4g, g5b, g5g, g6b, g6g]:
    if i % k == 0:
        room += i // k
    else:
        room += i // k + 1

print(room)

