N = int(input())
A = list(map(int, input().split()))
P = [0]*(N+9)
Q = [0]*(N+9)
for i in range(N):
  P[i+1] = max(P[i], A[i])
for i in range(N):
  Q[i+1] = max(Q[i], A[-(i+1)])
D = int(input())
for i in range(D):
  L, R = map(int, input().split())
  print(max(P[L-1], Q[N-R]))
