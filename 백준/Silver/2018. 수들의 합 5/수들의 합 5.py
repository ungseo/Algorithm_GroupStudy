N = int(input())
lst = [i for i in range(1,N+1)]

st = 0
ed = 1
cnt = 0 
sum = 0
while ed < N:
    if sum == N:
        cnt += 1
        st = ed
        ed += 1
        sum = 0
    elif sum > N:
        st = ed
        ed += 1
        sum = 0
    sum += lst[st]
    st += 1
    if st== 14:
        debug = 1
print(cnt+1)