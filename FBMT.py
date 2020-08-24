# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    d={}
    for i in range(n):
        s=input()
        if s not in d:
            d[s]=1
        else:
            d[s]+=1
    team=list(d.keys())
    
    if len(team)==1:
        print(team[0])
    elif len(team)==2:
        if d[team[0]]>d[team[1]]:
            print(team[0])
        elif d[team[1]]>d[team[0]]:
            print(team[1])
        else:
            print("Draw")
    else:
        print("Draw")
    
