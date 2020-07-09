# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    l=[]
    res=''
    for i in s:
        if i=='+' or i=='*' or i=='-' or i=='^' or i=='/' or i=='%':
            l.append(i)
        elif i==')':
            res+=l.pop()
        elif i=='(':
            continue
        else:
            res+=i
    print(res)
        
