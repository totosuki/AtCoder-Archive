import numpy as np
import sys
input = sys.stdin.buffer.readline

N = int(input())
A = np.array([0] + list(map(int, input().split())), dtype=np.int64)
MOD = 998244353

dp = np.zeros(N+1, dtype=np.int64)
dp[1] = 1

for i in range(1, N+1):
  dp[i] += dp[i-1]
  dp[i] %= MOD
  np.add.at(dp, np.arange(i+A[i], N+1, A[i]), dp[i])

answer = np.sum(dp) % MOD
print(answer)