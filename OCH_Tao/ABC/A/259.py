N,M,X,T,D = map(int,input().split())
if M>=X:
  print(T)
else:
  for i in range(X,M,-1):
    T-=D
  else:
    print(T)