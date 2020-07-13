# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    knight_movement=[]
    for i in range(n):
        x,y=map(int,input().split())
        knight_movement.append([x-2,y-1])
        knight_movement.append([x+2,y-1])
        knight_movement.append([x+2,y+1])
        knight_movement.append([x-2,y+1])
        knight_movement.append([x-1,y-2])
        knight_movement.append([x+1,y-2])
        knight_movement.append([x+1,y+2])
        knight_movement.append([x-1,y+2])
    king_movement=[]
    x,y=map(int,input().split())
    king_movement.append([x,y])
    king_movement.append([x-1,y])
    king_movement.append([x,y+1])
    king_movement.append([x+1,y])
    king_movement.append([x,y-1])
    king_movement.append([x-1,y])
    king_movement.append([x,y+1])
    king_movement.append([x-1,y-1])
    king_movement.append([x+1,y+1])
    king_movement.append([x-1,y+1])
    king_movement.append([x+1,y-1])
    result="YES"
    for i in king_movement:
        if i not in knight_movement:
            result="NO"
            break
    print(result)
