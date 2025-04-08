from itertools import accumulate
N = int(input())
A = ([0]+list(accumulate(map(int, input().split()))))
Q = int(input())
for i in range(Q):
  L, R = map(int, input().split())
  X = A[R]-A[L-1]
  if X > (R-L+1)-X:
    print("win")
  elif X < (R-L+1)-X:
    print("lose")
  else:
    print("draw")
