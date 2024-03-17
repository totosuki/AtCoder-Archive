N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 1 << 60

j = 0
for i in range(N):
  while j + 1 < M and B[j] <= A[i]:
    j += 1
  ans = min(ans, min(abs(A[i] - B[j]), abs(A[i] - B[j-1])))

print(ans)