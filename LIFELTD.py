# cook your dish here
t=int(input())
for _ in range(t):
    grid=[]
    for i in range(3):
        grid.append(input())
    #print(grid)
    c=0
    if grid[0][0]=='l' and grid[1][0]=='l' and grid[1][1]=='l' :
        c+=1
    if grid[0][1]=='l' and grid[1][1]=='l' and grid[1][2]=='l' :
        c+=1
    if grid[1][0]=='l' and grid[2][0]=='l' and grid[2][1]=='l' :
        c+=1
    if grid[1][1]=='l' and grid[2][1]=='l' and grid[2][2]=='l' :
        c+=1
    if c>=1:
        print("yes")
    else:
        print("no")
