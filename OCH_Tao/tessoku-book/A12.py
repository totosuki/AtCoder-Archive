N, K = map(int, input().split())
A = list(map(int, input().split()))
L = 1
R = int(1e9)
while L < R:
  M = (L+R)//2
  S = 0
  for i in range(N):
    S += M//A[i]
  if K <= S:
    R = M
  else:
    L = M+1
print(L)
