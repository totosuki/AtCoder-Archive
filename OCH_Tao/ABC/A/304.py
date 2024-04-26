N = int(input())
X = []
Y = []
for i in range(N):
  A,B = input().split()
  X.append(A)
  Y.append(int(B))
i = Y.index(min(Y))
print("\n".join(X[i:]+X[:i]))