import numpy as np
R,C = map(int,input().split())
X = np.expand_dims(np.array([True]),0)
for i in range(7):
  if i%2==0:
    X = np.pad(X,1,constant_values=False)
  else:
    X = np.pad(X,1,constant_values=True)
print("white" if X[R-1,C-1] else "black")