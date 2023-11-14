def dynamic_programming(N, S, A):
  dp = [[False]*(S+1) for _ in range(N+1)]
  dp[0][0] = True
  for i in range(1, N+1):
    a = A[i]
    for j in range(S+1):
      if j < a:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j] or dp[i-1][j-a]
  return dp

def dp_root(N, S, A, dp):
  root = []
  j = S
  for i in reversed(range(1, N+1)):
    a = A[i]
    if j >= a and dp[i-1][j-a]:
      root.append(i)
      j -= a
  return list(reversed(root))

def main():
  N, S = map(int, input().split())
  A = list(map(int, input().split()))
  A = [0] + A
  dp = dynamic_programming(N, S, A)
  if dp[N][S]:
    root = dp_root(N, S, A, dp)
    print(len(root))
    print(*root)
  else:
    print(-1)

main()