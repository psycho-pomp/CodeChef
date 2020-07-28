# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    d={}
    total=0
    for i in range(n):
        s=input()
        if s not in d:
            c=2
            for i in range(1,len(s)):
                if s[i]=='j' and (s[i-1]=='k' or s[i-1]=='j'):
                    c+=4
                elif s[i]=='k' and (s[i-1]=='j' or s[i-1]=='k'):
                    c+=4
                elif s[i]=='d' and (s[i-1]=='f' or s[i-1]=='d'):
                    c+=4
                elif s[i]=='f' and (s[i-1]=='d' or s[i-1]=='f'):
                    c+=4
                else:
                    c+=2
            d[s]=c
        else:
            c=d[s]//2
        
        total+=c
    print(total)
            
                    
                
                
            
