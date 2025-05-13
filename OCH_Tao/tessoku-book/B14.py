from itertools import combinations
from sys import exit
N, K = map(int, input().split())
A = list(map(int, input().split()))
P = set()
Q = set()
for i in range(N//2):
  P.update([sum(j) for j in combinations(A[:N//2], i+1)])
for i in range(N-N//2):
  Q.update([sum(j) for j in combinations(A[N//2:], i+1)])
if K in P or K in Q:
  print("Yes")
else:
  for i in P:
    if K-i in Q:
      print("Yes")
      break
  else:
    print("No")
