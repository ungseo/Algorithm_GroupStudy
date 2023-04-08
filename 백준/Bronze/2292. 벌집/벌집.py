n = int(input())

s = 0
rst = 1
while 1:
    rst += 6 * s
    if rst >= n:
        print(s+1)
        break
    s += 1