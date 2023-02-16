N = int(input())
A = list(map(int,input().split()))
A.sort()
k = -1
cnt = 0

# while k < N - 1:
#     st = 0 
#     ed = N - 1
#     k += 1
for k in range(N):
    st = 0
    ed = N - 1    
    while st < ed:
        if A[st] + A[ed] == A[k]:
            if st != k and ed != k:
                cnt += 1
                break
            elif st == k:
                st += 1
            elif ed == k:
                ed -= 1
            
        elif A[st] + A[ed] > A[k]:
            ed -= 1
        else:
            st += 1
    
print(cnt)