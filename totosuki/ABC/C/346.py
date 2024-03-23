N, K = map(int, input().split())
A = list(map(int, input().split()))
A = list(set(A))
A.sort()
B = []

for i in range(len(A)):
  if A[i] > K:
    break
  else:
    B.append(A[i])

sm = (1 + K) * K // 2

print(sm - sum(B))
