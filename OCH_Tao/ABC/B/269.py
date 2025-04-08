import numpy as np
S = []
for i in range(10):
  S.append(list(input()))
S = np.array(S)
X = np.argwhere(S=="#")
A = np.min(X,axis=0)[0]+1
B = np.max(X,axis=0)[0]+1
C = np.min(X,axis=0)[1]+1
D = np.max(X,axis=0)[1]+1
print(A,B)
print(C,D)