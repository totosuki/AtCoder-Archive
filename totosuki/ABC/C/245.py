N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[False] * 2 for _ in range(N)]
dp[0] = [True, True]

for i in range(1, N):
  if (dp[i-1][0] and abs(A[i] - A[i-1]) <= K) or (dp[i-1][1] and abs(A[i] - B[i-1]) <= K):
    dp[i][0] = True
  if (dp[i-1][0] and abs(B[i] - A[i-1]) <= K) or (dp[i-1][1] and abs(B[i] - B[i-1]) <= K):
    dp[i][1] = True

print("Yes") if dp[N-1][0] or dp[N-1][1] else print("No")