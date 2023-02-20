paper = [[0 for _ in range(100)] for _ in range(100)]
ea = int(input())
for i in range(ea):
    a, b = map(int,input().split())

    for i in range(10):
        for j in range(10):
            paper[90-b+i][a+j] += 1

    sum = 0
    for i in range(100):
        for j in range(100):
            if paper[i][j] >= 1:
                sum += 1

print(sum)
