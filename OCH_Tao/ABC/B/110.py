N,M,X,Y = map(int,input().split())
x = sorted(list(map(int,input().split())))
y = sorted(list(map(int,input().split())))
if max(x)<min(y) and max(x)>X and min(y)<Y:
  print("No War")
else:
  print("War")