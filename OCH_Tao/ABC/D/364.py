N,Q = map(int,input().split())
A = list(map(int,input().split()))
for i in range(Q):
  B,K = map(int,input().split())
  X = sorted(map(lambda x:abs(x-B),A))
  print(X[K-1])