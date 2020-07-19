# cook your dish here
t=int(input())
for i in range(t):
    s=input()
    res=''
    flag=s[0]
    temp=0
    for i in s:
        if i!=flag:
            res+=flag+str(temp)
            flag=i
            
            temp=1
        else:
            temp+=1
    res+=flag+str(temp)
    if len(res)<len(s):
        print("YES")
    else:
        print("NO")
