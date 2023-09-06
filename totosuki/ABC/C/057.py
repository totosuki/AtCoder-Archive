import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
now = sum(A[:K])
rslt = now

for i in range(1, N - K + 1):
  now -= A[i-1]
  now += A[i + K - 1]
  rslt += now

print(rslt)