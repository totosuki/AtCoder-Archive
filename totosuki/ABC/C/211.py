import sys
input = sys.stdin.buffer.readline

chokudai = {"c", "h", "o", "k", "u", "d", "a", "i"}
S = input().decode().strip()
dp = [[1] + [0] * 8 for _ in range(len(S))]

for i in range(len(S)):
  dp[i] = dp[i-1]

  if S[i] in chokudai:
    j = "chokudai".index(S[i])
    dp[i][j+1] += dp[i-1][j] 
    dp[i][j+1] %= 10**9 + 7

print(dp[len(S)-1][8])