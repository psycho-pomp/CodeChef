t=int(input())
for _ in range(t):
    s=input()
    flag=1
    for i in range(0,len(s),2):
        if s[i:i+2]=='AA' or s[i:i+2]=='BB':
            flag=0
            break
    if flag:
        print('yes')
    else:
        print('no')
