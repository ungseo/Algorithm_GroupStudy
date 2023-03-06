T= int(input())

for i in range(T):
    cal = str(input())
    year, month,day = cal[:4],cal[4:6],cal[6:8]
    if month in ['04','06','09','11'] :
        if int(day) <= 0 or int(day) >=31 :
            print('#'+str(i+1),-1)
        else :
            print('#'+str(i+1)+' '+year+'/'+month+'/'+day)
    elif month == '02' :
        if int(day) <= 0 or int(day) >=29 :
            print('#'+str(i+1),-1)
        else :
            print('#'+str(i+1)+' '+year+'/'+month+'/'+day)
    elif month in ['01','03','05','07','08','10','12']:
        if int(day) <= 0 or int(day) >=32 :
            print('#'+str(i+1),-1)
        else:
            print('#'+str(i+1)+' '+year+'/'+month+'/'+day)
    else:
        print('#'+str(i+1),-1)