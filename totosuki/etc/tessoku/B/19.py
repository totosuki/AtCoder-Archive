import sys
input = sys.stdin.buffer.readline

INF = 1 << 60
N, W = map(int, input().split())
w = [0] * (N+1)
v = [0] * (N+1)
for i in range(1, N+1): w[i], v[i] = map(int, input().split())

dp = [[INF] * (1000 * N + 1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
  for j in range(1000 * N + 1):
    if j < v[i]:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i]] + w[i])

rslt = 0

for j in range(1000 * N + 1):
  if dp[N][j] <= W:
    rslt = j

print(rslt)