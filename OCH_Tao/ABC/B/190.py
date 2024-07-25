N,S,D = map(int,input().split())
for i in range(N):
  X,Y = map(int,input().split())
  if X<S and Y>D:
    print("Yes")
    break
else:
  print("No")