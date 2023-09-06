N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
li = [0] * 100005

for i in range(1, N+1):
  li[i] = li[i-1] + A[i]

for _ in range(Q):
  L, R = map(int, input().split())
  rslt = li[R] - li[L-1]
  print(rslt)