from math import sqrt
N,D = map(int,input().split())
X = []
for i in range(N):
  X.append(list(map(int,input().split())))
cnt = 0
for i in range(N-1):
  A = X[i]
  for j in range(i+1,N):
    B = X[j]
    tmp = 0
    for k in range(D):
      tmp+=(A[k]-B[k])**2
    tmp=sqrt(tmp)
    if tmp%1==0:
      cnt+=1
print(cnt)