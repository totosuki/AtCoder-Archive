N,M = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
  X = list(map(int,input().split()))
  for j in range(M):
    A[j]-=X[j]
print("Yes" if all([i<=0 for i in A]) else "No")