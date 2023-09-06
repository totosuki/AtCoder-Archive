import sys
input = sys.stdin.buffer.readline

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
dp = [0] * N
dp[0] = T[0]

for i in range(1, N):
  dp[i] = min(dp[i-1] + S[i-1], T[i])

for i in range(N-1):
  dp[i] = min(dp[i-1] + S[i-1], dp[i])

[print(dp[i]) for i in range(N)]