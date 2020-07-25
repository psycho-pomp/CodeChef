# cook your dish here
n=int(input())
x=input()
res=0
for i in range(n-1,-1,-1):
    if x[i]=='0':
        res+=1
    elif x[i]=='1':
        break
print(res)
        
