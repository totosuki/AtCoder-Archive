N,X = map(int,input().split())
L = [0]*N
L[X-1]=1
A = list(map(int,input().split()))
while True:
  X=A[X-1]
  if L[X-1]!=1:
    L[X-1]=1
  else:
    break
print(sum(L))