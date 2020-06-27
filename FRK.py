n=int(input())
c=0
for i in range(n):
    s=input()
    if 'ch' in s or 'he' in s or 'ef' in s :
        c+=1
print(c)
