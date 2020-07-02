t= int(input())
for _ in range(t):
    n=int(input())
    matrix=[]
    for i in range(n):
        temp=[0]*n
        matrix.append(temp)
    
    x=1
    for k in range(n):
        for i in range(k+1):
            #print(i,k-i)
            matrix[i][k-i]=x
            x+=1
    y=n*n
    for k in range(n-1,0,-1):
        for i in range(n-1,k-1,-1):
            matrix[i][k-i+n-1]=y
            y-=1
      
        
    for q in range(n):
        print(*matrix[q])

