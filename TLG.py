# cook your dish here
max1=0
max2=0
player1,player2=0,0
n=int(input())
for i in range(n):
    s,t=map(int,input().split())
    player1+=s
    player2+=t
    if player1>player2:
        max1=max(max1,player1-player2)
    elif player2>player1:
        max2=max(max2,player2-player1)
if max1>max2:
    print(1,max1)
else:
    print(2,max2)
