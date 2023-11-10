N, M = map(int, input().split())
A = {int(input()) for _ in range(M)}
MOD = 1000000007

dp = [1] + [0] * N

for i in range(1, N+1):
  if i in A: continue
  dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[N])