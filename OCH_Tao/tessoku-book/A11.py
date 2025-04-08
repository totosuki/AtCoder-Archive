N, X = map(int, input().split())
A = list(map(int, input().split()))
L = 0
R = N-1
while L <= R:
  M = (L+R)//2
  if X == A[M]:
    print(M+1)
    break
  if X < A[M]:
    R = M-1
  if X > A[M]:
    L = M+1
