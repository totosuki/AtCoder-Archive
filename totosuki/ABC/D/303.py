import sys
input = sys.stdin.buffer.readline

X, Y, Z = map(int, input().split())
S = input().decode().rstrip()

dp = [[0] * 2 for _ in range(len(S))]
dp[0][0] = X if S[0] == "a" else Y
dp[0][1] = Z + Y if S[0] == "a" else Z + X

for i in range(1, len(S)):
  if S[i] == "a":
    dp[i][0] = min(dp[i-1][0] + X, dp[i-1][1] + Z + X)
    dp[i][1] = min(dp[i-1][1] + Y, dp[i-1][0] + Z + Y)
  else:
    dp[i][0] = min(dp[i-1][0] + Y, dp[i-1][1] + Z + Y)
    dp[i][1] = min(dp[i-1][1] + X, dp[i-1][0] + Z + X)

print(min(dp[len(S)-1]))