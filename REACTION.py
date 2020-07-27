# cook your dish here
t=int(input())
for _ in range(t):
    r,c=map(int,input().split())
    matrix=[]
    for i in range(r):
        matrix.append(list(map(int,input().split())))
    result='Stable'
    for i in range(r):
        for j in range(c):
            temp=0
            if 0<=i-1<r:
                temp+=1
            if 0<=j-1<c:
                temp+=1
            if 0<=j+1<c:
                temp+=1
            if 0<=i+1<r:
                temp+=1
            if matrix[i][j]>=temp:
                result='Unstable'
                break
    print(result)
        
            
                
        
    
