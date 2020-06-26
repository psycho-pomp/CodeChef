t=int(input())
for _ in range(t):
    s1=input()
    s2=input()
    ma=len(s1)
    mi=0
    for i in range(len(s1)):
        if 97<=ord(s1[i])<=122 and 97<=ord(s2[i])<=122:
            if s1[i]==s2[i]:
                ma-=1
            else:
                mi+=1
    print(mi,ma)
            
