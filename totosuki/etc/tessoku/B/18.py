import sys
input = sys.stdin.buffer.readline

N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[False] * (S+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
  for j in range(S+1):
    if dp[i-1][j]:
      dp[i][j] = True
      if j + A[i] <= S:
        dp[i][j+A[i]] = True

pos = S
rslt = []

if dp[N][S]:
  for i in reversed(range(1, N+1)):
    if pos - A[i] >= 0:
      if dp[i-1][pos-A[i]]:
        pos = pos-A[i]
        rslt.append(i)
  rslt.reverse()
  print(len(rslt))
  print(*rslt)
else:
  print(-1)