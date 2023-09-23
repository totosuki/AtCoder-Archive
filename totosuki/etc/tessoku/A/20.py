import sys
input = sys.stdin.buffer.readline

S = ["a"] + list(input().decode().rstrip())
T = ["a"] + list(input().decode().rstrip())

dp = [[0] * (len(T)) for _ in range(len(S))]

for i in range(1, len(S)):
  for j in range(1, len(T)):
    Si, Tj = S[i], T[j]
    if Si == Tj:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(S)-1][len(T)-1])