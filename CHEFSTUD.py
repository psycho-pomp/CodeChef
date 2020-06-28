t=int(input())
for _ in range(t):
    s=input()
    if len(s)<4:
        print(0)
    else:
        x=0
        for i in range(len(s)-3):
            if s[i:i+4]=='><><':
                x+=1
        print(x)
