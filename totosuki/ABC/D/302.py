import sys
input = sys.stdin.buffer.readline

N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
rslt = -1

j = 0

for i in range(N):
  while j + 1 < M:
    if B[j+1] - A[i] <= D:
      j += 1
    else:
      break

  if abs(A[i] - B[j]) <= D:
    rslt = max(rslt, A[i] + B[j])

print(rslt)