from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

A_sorted = sorted(A)
d = defaultdict(int)

for i in range(N):
  d[A_sorted[i]] = d[A_sorted[i-1]]
  d[A_sorted[i]] += A_sorted[i]

mx = d[A_sorted[-1]]

print(*[mx - d[A[i]] for i in range(N)])