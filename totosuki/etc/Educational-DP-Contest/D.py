import sys
input = sys.stdin.buffer.readline

N, W = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dp = [[-float("inf")] * (W+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
  w, v = data[i-1]
  
  for j in range(W + 1):
    dp[i][j] = dp[i-1][j]

  for j in range(W + 1 - w):
    dp[i][j+w] = max(dp[i-1][j+w], dp[i-1][j] + v)

print(max(dp[N]))