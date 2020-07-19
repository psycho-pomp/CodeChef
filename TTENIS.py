# cook your dish here
t=int(input())
for i in range(t):
    s=input()
    chef=0
    other=0
    flag=''
    for i in s:
        if i=='1':
            chef+=1
        else:
            other+=1
        if flag != 'duece':
            if chef==10 and other==10:
                flag='duece'
            if chef>=11:
                print('WIN')
                break
            elif other>=11:
                print("LOSE")
                break
        else:
            if chef-other==2:
                print("WIN")
                break
            elif other-chef==2:
                print('LOSE')
                break
            
                
            
