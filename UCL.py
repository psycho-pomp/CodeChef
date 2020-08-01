# cook your dish here
t=int(input())
for _ in range(t):
    d={}
    for i in range(12):
        hometeam,hometeam_goals,vs,awayteam_goals,awayteam=input().split()
        hometeam_goals=int(hometeam_goals)
        awayteam_goals=int(awayteam_goals)
        if hometeam not in d:
            d[hometeam]=[0]*2
        if awayteam not in d:
            d[awayteam]=[0]*2
        d[hometeam][1]+=(hometeam_goals-awayteam_goals)
        d[awayteam][1]+=(-hometeam_goals+awayteam_goals)
        if hometeam_goals>awayteam_goals:
            d[hometeam][0]+=3
        elif awayteam_goals>hometeam_goals:
            d[awayteam][0]+=3
        else:
            d[hometeam][0]+=1
            d[awayteam][0]+=1
    final=sorted(d.items(),key=lambda x:(x[1][0],x[1][1]),reverse=True)
    print(final[0][0],final[1][0])
            
        
