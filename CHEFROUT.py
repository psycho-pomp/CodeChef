# cook your dish here
t=int(input())
for _ in range(t):
    
    s=input()
    states={'C':0,'E':1,'S':2}
    result='yes'
    flag=states[s[0]]
    for i in s:
        if states[i]<flag:
            result='no'
            break
        else:
            flag=states[i]
    print(result)
        
        
    
