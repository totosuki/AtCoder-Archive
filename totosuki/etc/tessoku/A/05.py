N, K = map(int, input().split())
rslt = 0

for i in range(1, N+1):
  for j in range(1, N+1):
    if 1 <= K - (i + j) <= N:
      rslt += 1

print(rslt)