T = int(input())
for i in range(1,T+1):
    A, B = input().split(' ')
    if int(A) < int(B) :
        print('#'+str(i)+' <')
    elif int(A) == int(B) :
        print('#'+str(i)+' =')
    else :
        print('#'+str(i)+' >')
        