import collections
N = int(input())
A = list(map(int,input().split()))
W = list(map(int,input().split()))
D = collections.Counter(A)
L = [[] for i in [0]*N]
cnt = 0
for i in range(N):
  L[A[i]-1].append(W[i])
for i in range(N):
  X=sorted(L[i])
  if (Y:=D.get(i+1,0))>1:
    cnt+=sum(X[:Y-1])
print(cnt)