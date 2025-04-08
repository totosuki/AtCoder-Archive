N,M = map(int,input().split())
X = [set() for _ in range(N)]
for i in range(M):
  k,*x = map(int,input().split())
  for j in x:
    X[j-1].update(x)
print("Yes" if all([len(i)==N for i in X]) else "No")