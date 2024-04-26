X,Y,N = map(int,input().split())
if 3*X<Y:
  print(X*N)
else:
  cnt=0
  while N>2:
    cnt+=Y
    N-=3
  else:
    print(cnt+N*X)