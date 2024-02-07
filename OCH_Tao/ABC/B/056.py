W,A,B = map(int,input().split())
x = [A,B]
x.sort()
if x[0]+W>x[1]:
  print(0)
else:
  print(x[1]-x[0]-W)