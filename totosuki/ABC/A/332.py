N, S, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
rslt = 0
for d in data:
  p, q = d
  rslt += p * q

if rslt >= S:
  print(rslt)
else:
  print(rslt + K)