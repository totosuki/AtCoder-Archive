N, K = map(int, input().split())
a = K
if N == 1:
  b = 1
else:
  b = (K-1) ** (N-1)
print(a * b)