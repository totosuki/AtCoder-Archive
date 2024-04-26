N,Q = map(int,input().split())
T = list(map(int,input().split()))
L = [1]*N
for i in T:
  if L[i-1]==1:
    L[i-1]=0
  else:
    L[i-1]=1
print(sum(L))