N,A,X,Y = map(int,input().split())
if N > A:
  print(N*X - (N-A)*(X-Y))
else:
  print(N*X)