import sys
input = sys.stdin.buffer.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * 3 for _ in range(N)]
dp[0] = data[0]

for i in range(1, N):
  a, b, c = data[i]
  
  dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a
  dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b
  dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c

print(max(dp[N-1]))