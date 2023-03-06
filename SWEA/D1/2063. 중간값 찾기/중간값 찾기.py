N= int(input())
M = input()
m = list(map(int,M.split(' ')))
m.sort()
x=int( (N + 1)/2-1)
print(m[x])

         