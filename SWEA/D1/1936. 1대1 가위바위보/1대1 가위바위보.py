m= input()
A,B = m.split()
result = (int(A),int(B))


A_win = [ (1,3), (2,1) , (3,2) ]

if result in A_win :
    print('A')
else :
    print('B')
    