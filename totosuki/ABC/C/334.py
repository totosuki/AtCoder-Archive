N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

dp = [[float('inf')] * (N+1) for _ in range(K+2)]
dp[0][0] = 0

for i in range(K):
    for j in range((i+1)//2+1):
        if dp[i][j] == float('inf'):
            continue
        if i+2 < K:
            dp[i+2][j+1] = min(dp[i+2][j+1], dp[i][j] + abs(A[i+2] - A[i+1]))
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

pairs = (2 * N - K) // 2

if (2 * N - K) % 2 == 0:
    print(min(dp[K][pairs], dp[K-1][pairs]))
else:
    print(min(dp[K][pairs], dp[K-1][pairs] + A[K-1]))