def dynamic_programming(N, D):
  dp = [[0]*(N+1) for _ in range(N+1)]
  for l in range(1, N+1):
    for r in reversed(range(l, N+1)):
      if l == 1 and r == N: # 初期地点は飛ばす
        continue
      elif l == 1:
        p, a = D[r+1]
        score = a if l <= p <= r else 0
        dp[l][r] = dp[l][r+1] + score
      elif r == N:
        p, a = D[l-1]
        score = a if l <= p <= r else 0
        dp[l][r] = dp[l-1][r] + score
      else:
        p1, a1 = D[r+1]
        p2, a2 = D[l-1]
        score1 = a1 if l <= p1 <= r else 0
        score2 = a2 if l <= p2 <= r else 0
        dp[l][r] = max(dp[l][r+1] + score1, dp[l-1][r] + score2)
  return dp

def main():
  N = int(input())
  D = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]
  dp = dynamic_programming(N, D)
  print(max([dp[i][i] for i in range(1, N+1)]))

main()