# 未AC
import numpy as np
N,T = map(int,input().split())
A = list(map(int,input().split()))
D = dict()
for i in range(T):
  D[A[i]]=i+1
X = np.arange(1,N**2+1).reshape((N,N))
cnt = []
flag = False
for x in range(N):
  if len([i for i in A if (i-1)//N==x])==N:
    flag=True
    cnt.append([N*x+i for i in range(1,N+1)])
else:
  for x in range(N):
    if len([i for i in A if (i-1)%N==x])==N:
      flag=True
      cnt.append([N*i+x+1 for i in range(N)])
  else:
    if set(n:=(np.diag(X))) <= set(A):
      flag=True
      cnt.append(list(n))
    elif set(n:=(np.diag(np.rot90(X)))) <= set(A):
      flag=True
      cnt.append(list(n))
tmp = N*N
if flag:
  for i in cnt:
    l = []
    for j in i:
      l.append(D[j])
    tmp=min(tmp,max(l))
  print(tmp)
else:
  print(-1)