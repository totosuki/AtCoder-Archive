def dynamic_programming(N, M, S, T):
  dp = [None] * (N+1)
  for i in range(1, M+1):
    if S[i] == T[i]:
      dp[i] = True
    else:
      dp[i] = False
  print(dp, 1)
  for i in range(2, N+1):
    tf_cnt = -1 # True Falseカウント 両方なったら交差してる
    for j in range(M):
      if i + j > N: break
      if S[i+j] == T[j+1]:
        tf_cnt = 1
      else:
        tf_cnt = 0
      if tf_cnt == 1 and dp[i+j] == True:
        dp[i+j] = True
      if tf_cnt == 0 and dp[i+j] == False:
        dp[i+j] = False
      if tf_cnt == 1 and dp[i+j] == None:
        dp[i:i+j+1] = [True] * (j+1)
    print(dp, i)
  return dp

def main():
  N, M = map(int, input().split())
  S = ["_"] + list(input())
  T = ["_"] + list(input())
  dp = dynamic_programming(N, M, S, T)
  print("Yes" if False not in dp[1:] else "No")

main()