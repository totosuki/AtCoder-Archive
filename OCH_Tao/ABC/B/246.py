from math import atan2,cos,sin
A,B = map(int,input().split())
D = atan2(B,A)
print(cos(D),sin(D))