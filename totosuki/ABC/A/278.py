N, K = map(int, input().split())
A = list(map(int, input().split()))
rslt = [a for a in A]
rslt = rslt[K:]
for _ in range(K):
  if len(rslt) < len(A):
    rslt.append(0)
print(*rslt)