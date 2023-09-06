X, Y, N = map(int, input().split())

if X*3 <= Y:
  print(N*X)
else:
  tmp = (N // 3) * Y
  tmp2 = (N%3) * X
  print(tmp + tmp2)