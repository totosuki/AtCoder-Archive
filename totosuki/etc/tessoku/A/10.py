import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
D = int(input())

# 累積和(最大値)
cum_L = [0] * N
cum_R = [0] * N
cum_L[0] = A[0]
cum_R[N-1] = A[N-1]

for i in range(1, N):
  cum_L[i] = max(cum_L[i-1], A[i])
for i in reversed(range(N-1)):
  cum_R[i] = max(cum_R[i+1], A[i])

for _ in range(D):
  L, R = map(int, input().split())
  print(max(cum_L[L-2], cum_R[R]))