import sys
input = sys.stdin.buffer.readline

N, W = map(int, input().split())
WV = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]
INF = -float("inf")

dp = [[INF] * (W+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
  for j in range(W+1):
    if j >= WV[i][0]:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-WV[i][0]] + WV[i][1])
    else:
      dp[i][j] = dp[i-1][j]

print(max(dp[N]))

# for i in range(1, N+1):
#   for j in range(W+1):
#     if j + WV[i][0] <= W:
#       dp[i][j] = max(dp[i-1][j], dp[i][j])
#       dp[i][j+WV[i][0]] = max(dp[i-1][j]+WV[i][1], dp[i][j+WV[i][0]])
#     else:
#       dp[i][j] = max(dp[i-1][j], dp[i][j])