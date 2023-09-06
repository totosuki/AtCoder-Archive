import sys
input = sys.stdin.buffer.readline

N = int(input())
taka = 0 # X
aoki = 0 # Y
r = 10**6 # range

dp = [[-1] * r for _ in range(N+1)]
dp[0][0] = 0

# knapsack dynamic programming
for i in range(1, N+1):
  X, Y, Z = map(int, input().split())
  if X > Y:
    taka += Z
  else:
    aoki += Z

  for j in range(r):
    if dp[i-1][j] != -1:
      dp[i][j] = dp[i-1][j]
    
    if Y > X and dp[i-1][j] != -1:
      point = (Y - X) // 2 + 1 # 議席を獲得できる最低票数
      if dp[i][j+Z] == -1:
        dp[i][j+Z] = dp[i-1][j] + point
      else:
        dp[i][j+Z] = min(dp[i][j+Z], dp[i-1][j] + point)

win_point = (aoki - taka) // 2 + 1
rslt = 10**9

print(dp[N][win_point : win_point+100])

for i in range(win_point, r):
  if dp[N][i] != -1:
    rslt = min(rslt, dp[N][i])

if taka > aoki:
  print(0)
else:
  print(rslt)