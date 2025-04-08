import numpy as np
H, W = map(int, input().split())
A = []
for i in range(H):
  A.append(list(input()))
A = np.array(A)
B = []
for i in range(H):
  B.append(list(input()))
B = np.array(B)
for i in np.ndindex(H, W):
  if np.all(np.roll(A, i, axis=(0, 1)) == B):
    print("Yes")
    break
else:
  print("No")
