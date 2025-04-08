import numpy as np
N = int(input())
A = np.array(list(map(int,input().split())))
X = np.diff(A)
cnt = N
cnt+=len(X)
for i in range(N-2):
  for j in range(i+1,N-1):
    if len(set(X[i:j+1]))==1:
      cnt+=1
print(cnt)