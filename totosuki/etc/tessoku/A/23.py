def dynamic_programming(N, M, A):
  INF = float("inf")
  dp = [[INF]*(2**N) for _ in range(M+1)]
  dp[0][0] = 0
  for i in range(1, M+1):
    for j in range(2**N):
      res = 0
      for k in range(N):
        if (j >> k) & 1 or A[i][k] == 1:
          res += 2 ** k
      dp[i][j] = min(dp[i][j], dp[i-1][j])
      dp[i][res] = min(dp[i][res], dp[i-1][j] + 1)
  return dp


def main():
  N, M = map(int, input().split())
  A = [[0]] + [list(map(int, input().split())) for _ in range(M)]
  dp = dynamic_programming(N, M, A)
  print(dp[M][2**N-1] if dp[M][2**N-1] != float("inf") else -1)

main()