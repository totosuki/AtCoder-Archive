import numpy as np
N = int(input())
X = np.zeros((1509, 1509), dtype=np.int64)
for i in range(N):
  A, B, C, D = map(int, input().split())
  X[A, B] += 1
  X[C, D] += 1
  X[A, D] -= 1
  X[C, B] -= 1
X = X.cumsum(axis=0)
X = X.cumsum(axis=1)
print(np.count_nonzero(X))
