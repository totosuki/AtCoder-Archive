N, M, X = map(int, input().split())
A = list(map(int, input().split()))
rslt = []

cost = 0
for i in range(0, X):
  if i in A:
    cost += 1
rslt.append(cost)

cost = 0
for i in range(X, N):
  if i in A:
    cost += 1
rslt.append(cost)

print(min(rslt))