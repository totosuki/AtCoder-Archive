def dynamic_programming(N, A, B):
  dp = [0] * (N+1)
  dp[2] = A[2]
  for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])
  return dp

def dp_root(N, A, B, dp):
  root = [N]
  i = N
  while i > 1:
    if dp[i-1] + A[i] == dp[i]:
      root.append(i-1)
      i -= 1
    else:
      root.append(i-2)
      i -= 2
  return root

def main():
  N = int(input())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  A = [0, 0] + A
  B = [0, 0, 0] + B
  dp = dynamic_programming(N, A, B)
  root = dp_root(N, A, B, dp)
  print(len(root))
  print(*reversed(root))

main()