def dynamic_programming(N, A, B):
  INF = -float("inf")
  dp = [INF] * (N+1)
  dp[1] = 0
  for i in range(1, N):
    a = A[i]
    b = B[i]
    dp[a] = max(dp[i]+100, dp[a])
    dp[b] = max(dp[i]+150, dp[b])
  return dp

def main():
  N = int(input())
  A = [0] + list(map(int, input().split()))
  B = [0] + list(map(int, input().split()))
  dp = dynamic_programming(N, A, B)
  print(dp[N])

main()