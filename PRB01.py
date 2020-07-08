# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    result='yes'
    if n>1:
        for i in range(2,n//2):
            if n%i==0:
                result="no"
                break
    
        print(result)
    else:
        print("no")
