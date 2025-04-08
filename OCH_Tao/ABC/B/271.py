N,Q = map(int,input().split())
L = []
for i in range(N):
  x,*a = map(int,input().split())
  L.append(a)
for i in range(Q):
  S,T = map(int,input().split())
  print(L[S-1][T-1])