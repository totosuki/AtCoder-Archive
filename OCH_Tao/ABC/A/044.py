N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if N - K <= 0:
  print(N*X)
else:
  print(K*X+(N-K)*Y)