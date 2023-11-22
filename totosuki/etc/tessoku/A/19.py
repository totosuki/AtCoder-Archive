def dynamic_programming(N, W, data):
  INF = -float("inf")
  dp = [[INF]*(W+1) for _ in range(N+1)]
  dp[0][0] = 0
  for i in range(1, N+1):
    w, v = data[i]
    for j in range(W+1):
      if j < w:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])
  return dp

def main():
  N, W = map(int, input().split())
  data = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]
  dp = dynamic_programming(N, W, data)
  print(max(dp[N]))

main()