N, M, X, T, D = map(int, input().split())
if X <= M:
  print(T)
else:
  rslt = T - ((X - M) * D)
  print(rslt)