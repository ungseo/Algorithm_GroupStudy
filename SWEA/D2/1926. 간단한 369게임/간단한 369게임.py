n = int(input())
ans = []
for i in range(1, n + 1):
    cnt = 0
    if '3' in str(i):
        cnt += str(i).count('3')
    if '6' in str(i):
        cnt += str(i).count('6')
    if '9' in str(i):
        cnt += str(i).count('9')
    if cnt > 0:
        ans.append('-' * cnt)
    else:
        ans.append(i)

print(*ans)
