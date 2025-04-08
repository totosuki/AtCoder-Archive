from itertools import accumulate
N, Q = map(int, input().split())
A = [0] + list(accumulate(map(int, input().split())))
for i in range(Q):
  L, R = map(int, input().split())
  print(A[R]-A[L-1])
