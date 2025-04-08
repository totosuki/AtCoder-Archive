N,M,T = map(int,input().split())
A = list(map(int,input().split()))
D = dict()
for i in range(M):
  X,Y = map(int,input().split())
  D[X] = Y
for i in range(1,N):
  T += D.get(i,0)
  T -= A[i-1]
  if T<=0:
    print("No")
    break
else:
  print("Yes")