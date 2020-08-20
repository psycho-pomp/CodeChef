# cook your dish here
# cook your dish here
from sys import stdin,stdout
def get_ints():return map(int,stdin.readline().strip().split())
def get_array():return list(map(int,stdin.readline().strip().split()))
def get_string():return stdin.readline().strip()
def get_int():return int(stdin.readline().strip())
def op(c):return stdout.write(c)
from collections import Counter
t=get_int()
for i in range(t):
    s=get_string()
    freq=Counter(s)
    if 'D' not in freq:
        freq['D']=0
    if 'U' not in freq:
        freq['U']=0
    if 'L' not in freq:
        freq['L']=0
    if 'R' not in freq:
        freq['R']=0
    #print(freq)
    x,y=get_ints()
    q=get_int()
    for i in range(q):
        x1,y1=get_ints()
        no_ud=y1-y
        no_lr=x1-x
        #print(no_ud,no_lr)
        if (no_ud<=0 and abs(no_ud)<=freq['D']) and (no_lr<=0 and abs(no_lr)<=freq['L']):
            op("YES "+str(abs(no_lr)+abs(no_ud))+"\n")
        elif (no_ud<=0 and abs(no_ud)<=freq['D']) and (no_lr>=0 and abs(no_lr)<=freq['R']):
            op("YES "+str(abs(no_lr)+abs(no_ud))+"\n")
        elif (no_ud>=0 and abs(no_ud)<=freq['U']) and (no_lr<=0 and abs(no_lr)<=freq['L']):
            op("YES "+str(abs(no_lr)+abs(no_ud))+"\n")
        elif (no_ud>=0 and abs(no_ud)<=freq['U']) and (no_lr>=0 and abs(no_lr)<=freq['R']):
            op("YES "+str(abs(no_lr)+abs(no_ud))+"\n")
        else:
            op("NO"+"\n")
            
            
