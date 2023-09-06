N, A, X, Y = map(int, input().split())
if N > A:
  print((A * X) + Y*(N-A))
else:
  print(N * X)