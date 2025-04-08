N = int(input())
L = [[0]*1509 for _ in range(1509)]
for i in range(N):
  X, Y = map(int, input().split())
  L[X][Y] += 1
for i in range(1, 1501):
  for j in range(1, 1501):
    L[i][j] += L[i][j-1]
for i in range(1, 1501):
  for j in range(1, 1501):
    L[j][i] += L[j-1][i]
Q = int(input())
for i in range(Q):
  A, B, C, D = map(int, input().split())
  print(L[C][D]+L[A-1][B-1]-L[A-1][D]-L[C][B-1])
