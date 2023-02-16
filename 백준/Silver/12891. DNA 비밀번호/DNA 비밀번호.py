def check(a,b):
    cnt = 0
    for i in range(4):
        if a[i] >= b[i]:   ## b = min ACGT
            cnt += 1
    if cnt == 4:
        return 1
    return 0
    
    
ll, lp = map(int,input().split())
DNAst = input()
min_ACGT = list(map(int,input().split()))
ACGT_cnt = [0] * 4
result = 0

for i in range(lp):
    if DNAst[i] == 'A':
        ACGT_cnt[0] += 1
    elif DNAst[i] == 'C':
        ACGT_cnt[1] += 1
    elif DNAst[i] == 'G':
        ACGT_cnt[2] += 1
    else:
        ACGT_cnt[3] += 1
result += check(ACGT_cnt,min_ACGT)

for i in range(ll-lp):
    # 왼쪽 값 빼기
    if DNAst[i] == 'A':
        ACGT_cnt[0] -= 1
    elif DNAst[i] == 'C':
        ACGT_cnt[1] -= 1
    elif DNAst[i] == 'G':
        ACGT_cnt[2] -= 1
    else:
        ACGT_cnt[3] -= 1
    # 오른쪽값 더하기
    if DNAst[i+lp] == 'A':
        ACGT_cnt[0] += 1
    elif DNAst[i+lp] == 'C':
        ACGT_cnt[1] += 1
    elif DNAst[i+lp] == 'G':
        ACGT_cnt[2] += 1
    else:
        ACGT_cnt[3] += 1

    result += check(ACGT_cnt,min_ACGT)

print(result)