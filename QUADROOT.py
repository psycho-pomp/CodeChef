import math
A=float(input())
B=float(input())
C=float(input())
D=B*B-4*A*C
x1=(-B+(math.sqrt(D)))/(2*A)
x2=(-B-(math.sqrt(D)))/(2*A)
print(x1)
print(x2)
