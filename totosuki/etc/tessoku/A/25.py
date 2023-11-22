def dynamic_programming(H, W, C):
  dp = [[0] * (W+1) for _ in range(H+1)]
  dp[1][1] = 1
  for i in range(1, H+1):
    for j in range(1, W+1):
      if i == 1 and j == 1:
        continue
      elif C[i][j] == "#":
        dp[i][j] = 0
      elif i == 1:
        dp[i][j] = dp[i][j-1]
      elif j == 1:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
  return dp

def main():
  H, W = map(int, input().split())
  C = [["_"]] + [["_"] + list(input()) for _ in range(H)]
  dp = dynamic_programming(H, W, C)
  print(dp[H][W])

main()