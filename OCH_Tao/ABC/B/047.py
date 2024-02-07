W,H,N = map(int,input().split())
p = [[0,0],[W,H]]
for i in range(N):
  x,y,a = map(int,input().split())
  if a==1:
    if p[0][0]<x:
      p[0][0]=x
  elif a==2:
    if p[1][0]>x:
      p[1][0]=x
  elif a==3:
    if p[0][1]<y:
      p[0][1]=y
  else:
    if p[1][1]>y:
      p[1][1]=y
if (p[1][0]-p[0][0])>0 and (p[1][1]-p[0][1])>0:
  S=(p[1][0]-p[0][0])*(p[1][1]-p[0][1])
else:
  S=0
print(S)