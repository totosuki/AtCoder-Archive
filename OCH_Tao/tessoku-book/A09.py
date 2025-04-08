import numpy as np
H, W, N = map(int, input().split())
X = np.zeros((H+9, W+9), dtype=np.int64)
for i in range(N):
  A, B, C, D = map(int, input().split())
  X[A, B] += 1
  X[C+1, D+1] += 1
  X[A, D+1] -= 1
  X[C+1, B] -= 1
X = X.cumsum(axis=0)
X = X.cumsum(axis=1)
for i in range(1, H+1):
  print(*X[i, 1:W+1])
