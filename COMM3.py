# cook your dish here
import math
t=int(input())
for _ in range(t):
    r=int(input())
    chefX,chefY=map(int,input().split())
    headX,headY=map(int,input().split())
    sousX,sousY=map(int,input().split())
    chef_head=math.sqrt((headX-chefX)**2+(headY-chefY)**2)
    chef_sous=math.sqrt((sousX-chefX)**2+(sousY-chefY)**2)
    head_sous=math.sqrt((sousX-headX)**2+(sousY-headY)**2)
    c=0
    if chef_sous<=r:
        c+=1
    if head_sous<=r:
        c+=1
    if chef_head<=r:
        c+=1
    if c>=2:
        print("yes")
    else:
        print("no")
