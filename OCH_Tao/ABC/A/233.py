from math import ceil
X,Y = map(int,input().split())
if X>=Y:
  print(0)
else:
  print(ceil((Y-X)/10))