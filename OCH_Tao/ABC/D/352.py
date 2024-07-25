N,K = map(int,input().split())
P = list(map(int,input().split()))
L = []
cnt = N
for i in range(N):
  L.append(P.index(i+1))
for i in range(N-K):
  X = L[i:i+K]
  cnt = min(max(X)-min(X),cnt)
print(cnt)