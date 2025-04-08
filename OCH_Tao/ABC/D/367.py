from itertools import accumulate
N,M = map(int,input().split())
A = list(map(lambda x:int(x)%M,input().split()))
cnt = 0
for i in range(N):
  X = A[i:]+A[:i]
  for j in accumulate(X):
    if j%M==0:
      cnt+=1
print(cnt)