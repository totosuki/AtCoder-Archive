N, K = map(int, input().split())
rslt = 0

for n in range(1, N+1):
  for k in range(1, K+1):
    rslt += int(str(n) + "0" + str(k))

print(rslt)