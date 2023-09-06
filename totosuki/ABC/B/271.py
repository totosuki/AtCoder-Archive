N, Q = map(int, input().split())
L = []
A = []
for _ in range(N):
  tmp = list(map(int, input().split()))
  L.append(tmp[0])
  A.append(tmp[1:])
queries = [list(map(int, input().split())) for _ in range(Q)]
for query in queries:
  print(A[query[0]-1][query[1]-1])