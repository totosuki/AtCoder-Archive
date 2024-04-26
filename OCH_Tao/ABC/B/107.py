import numpy as np
H,W = map(int,input().split())
A = np.empty(W,dtype=np.unicode_)
for i in range(H):
  a = np.array(list(input()))
  A = np.vstack([A,a])
A = A[:,np.any(A=="#",axis=0)]
A = A[np.any(A=="#",axis=1),:]
print("\n".join(["".join(i) for i in A]))