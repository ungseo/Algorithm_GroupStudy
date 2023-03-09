N=int(input())
lst=list(map(int, input().split()))
# 불가능한 경우 -1을 넣어야 하는데 번거로워서 기본값을 -1로 설정
rlt=[-1]*N
stack=[0]
for i in range(1,N):
     while stack and lst[stack[-1]]<lst[i]:
          rlt[stack.pop()]=lst[i]
     stack.append(i)
print(*rlt)