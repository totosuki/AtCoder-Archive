import sys
input = sys.stdin.buffer.readline

N, W = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dp = [[float("inf")] * (10**5+5) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
  w, v = data[i-1]
  
  for j in range(10**5+5):
    dp[i][j] = dp[i-1][j]
  
  for j in range(10**5+5 - v):
    dp[i][j+v] = min(dp[i-1][j+v], dp[i-1][j] + w)

rslt = 0

for j in range(10**5+5):
  if dp[N][j] <= W:
    rslt = j

print(rslt)