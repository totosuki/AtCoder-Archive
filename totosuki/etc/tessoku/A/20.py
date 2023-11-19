def dynamic_programming(N, M, S, T):
  dp = [[0]*(M+1) for _ in range(N+1)]
  for i in range(1, N+1):
    for j in range(1, M+1):
      if S[i] == T[j]:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  return dp

def main():
  S = ["_"] + list(input())
  T = ["_"] + list(input())
  N = len(S) - 1
  M = len(T) - 1
  dp = dynamic_programming(N, M, S, T)
  print(dp[N][M])

main()