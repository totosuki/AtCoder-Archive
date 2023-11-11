N, Q = map(int, input().split())
S = list(input())


B = [0] * (N)

for i in range(1, N):
  if S[i-1] == S[i]:
    B[i] = B[i-1] + 1
  else:
    B[i] = B[i-1]

for _ in range(Q):
  l, r = map(int, input().split())
  print(B[r-1] - B[l-1])