N,M = map(int,input().split())
X = [set() for _ in range(N)]
for i in range(M):
  A,B = map(int,input().split())
  X[A-1].add(B)
  X[B-1].add(A)
for i in X:
  print(len(i),*sorted(i),sep=" ")