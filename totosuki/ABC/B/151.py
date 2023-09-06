N, K, M = map(int, input().split())
A = list(map(int, input().split()))
rslt = -1

for i in range(K+1):
  a = (sum(A) + i) / N
  if a >= M:
    rslt = i
    break

print(rslt)