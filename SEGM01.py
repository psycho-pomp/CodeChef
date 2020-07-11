# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    
    if '1' in s:
        x=s.count('1')
        idx=s.index('1')
        if list(s[idx:idx+x])==['1']*x:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
