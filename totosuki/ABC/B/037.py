N, Q = map(int, input().split())
rslt = [0] * N

for _ in range(Q):
  L, R, T = map(int, input().split())
  for i in range(L-1, R):
    rslt[i] = T

[print(r) for r in rslt]