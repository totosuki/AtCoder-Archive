import numpy as np
N,K = map(int,input().split())
A = set(list(map(int,input().split())))
R = []
L = []
for i in range(1,N+1):
  if i in A:
    R.append(np.array(list(map(int,input().split()))))
  else:
    L.append(np.array(list(map(int,input().split()))))
ans = [np.inf]*len(L)
for i in R:
  for j in range(len(L)):
    ans[j]=min(ans[j],np.linalg.norm(i-L[j]))
print(max(ans))