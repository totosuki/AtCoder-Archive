import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
R = [0] * N
rslt = 0

for i in range(N-1):
  if i == 0:
    R[i] = 0
  else:
    R[i] = R[i-1]
  
  while R[i] < N-1 and A[R[i]+1] - A[i] <= K:
    R[i] += 1

for i in range(N-1):
  rslt += R[i] - i

print(rslt)