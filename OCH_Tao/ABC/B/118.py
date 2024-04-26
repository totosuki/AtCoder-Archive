N,M = map(int,input().split())
L = [0]*M
for i in range(N):
  A = list(map(int,input().split()))
  del A[0]
  for j in A:
    L[j-1]+=1
print(L.count(N))