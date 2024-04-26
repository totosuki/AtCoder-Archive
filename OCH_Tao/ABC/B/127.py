R,D,X = map(int,input().split())
for i in range(10):
  X = R*X-D
  print(X)