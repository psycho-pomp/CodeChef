t=int(input())
for _ in range(t):
    n=int(input())
    ans=''
    x=input()
    for i in range(1,n):
        s=input()
        for j in range(10):
            if x[j]==s[j]:
                ans+='0'
            else:
                ans+='1'
        x=ans
        ans=''
    print(x.count('1'))
