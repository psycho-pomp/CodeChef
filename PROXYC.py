import math
t=int(input())
for _ in range(t):
    d=int(input())
    s=input()
    mn=math.ceil((0.75*d))
    np=s.count("P")
    #print(mn,np)
    if np>=mn:
        print(0)
    else:
        if d>4:
            count=0
            for i in range(2,d-2):
                if s[i]=='A' and (s[i-1]=='P' or s[i-2]=='P') and (s[i+1]=='P' or s[i+2]=='P'):
                    count+=1
            #print(count)
            if np+count>=mn:
                print(mn-np)
            else:
                print(-1)
        else:
            print(-1)
        
    
    
