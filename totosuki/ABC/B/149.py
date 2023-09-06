A, B, K = map(int, input().split())

if A >= K:
  A -= K
  K = 0
elif A < K:
  K -= A
  A = 0
  if B >= K:
    B -= K
  elif B < K:
    B = 0

print(A, B)