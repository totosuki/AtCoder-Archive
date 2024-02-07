import numpy as np
N = int(input())
S = []
for i in range(N):
  S.append(list(input()))
ndS = np.array(S)
rotS = np.rot90(ndS,-1)
for i in range(N):
  print("".join(rotS[i]))