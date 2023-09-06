A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
rslt = 0
if S+T >= K:
  rslt += A*S - C*S
  rslt += B*T - C*T
  print(rslt)
else:
  rslt += A*S + B*T
  print(rslt)