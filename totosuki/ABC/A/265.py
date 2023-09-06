import math
X, Y, N = map(int, input().split())
rslt = 0
if X*3 > Y:
  rslt += math.floor(N / 3) * Y
  rslt += (N % 3) * X
  print(rslt)
else:
  rslt += N * X
  print(rslt)