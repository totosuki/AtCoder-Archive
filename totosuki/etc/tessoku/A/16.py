N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * N
dp[1] = A[1-1]

for i in range(2, N):
  dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + B[i-2])

print(dp[N-1])