N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())
for i in range(Q):
  X = int(input())
  L = 0
  R = N
  while L < R:
    M = (L+R)//2
    if A[M] < X:
      L = M+1
    else:
      R = M
  print(L)
