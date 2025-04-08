import numpy as np
N,K = map(int,input().split())
R = tuple(map(int,input().split()))
for i in np.ndindex(R):
  if (sum(i)+N)%K==0:
    print(*map(lambda x:x+1,i))