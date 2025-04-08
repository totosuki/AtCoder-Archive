X,Y,Z = map(int,input().split())
if (X>Y>0 and Z>Y) or (X<Y<0 and Z<Y):
  print(-1)
elif X>Y>0 or X<Y<0:
  print(abs(0-Z)+(abs(X-Z)))
else:
  print(abs(X))