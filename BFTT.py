# cook your dish here
t=int(input())
for _ in range(t):
    n=input()
    for i in range(int(n)+1,int(n)+1001):
        if str(i).count("3")>=3:
            print(i)
            break
