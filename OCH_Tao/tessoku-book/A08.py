from itertools import accumulate
H, W = map(int, input().split())
X = [[0]*(W+1)]
for i in range(H):
  X.append([0]+list(map(int, input().split())))
X = [list(accumulate(i)) for i in X]
for i in range(1, W+1):
  for j in range(1, H+1):
    X[j][i] = X[j-1][i]+X[j][i]
Q = int(input())
for i in range(Q):
  A, B, C, D = map(int, input().split())
  print(X[C][D]+X[A-1][B-1]-X[A-1][D]-X[C][B-1])
