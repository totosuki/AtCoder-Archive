N, K, P = map(int, input().split())
A = []
C = []

for i in range(N):
  tmp = list(map(int, input().split()))
  C.append(tmp[0])
  A.append(tmp[1:])

dp = [[[float("inf")] * (P+1) for _ in range(K)] for _ in range(N+1)]
for i in range(K):
  dp[0][i][0] = 0

for i in range(1, N+1):
  for j in range(K):
    a = A[i-1][j]
    c = C[i-1]
    for k in range(P+1):
      if k >= a:
        dp[i][j][k] = min(dp[i-1][j][k], dp[i-1][j][k-a] + c)
      else:
        dp[i][j][k] = dp[i-1][j][k]

ans = []

for k in range(K):
  ans.append(dp[N][k][P])

if max(ans) == float("inf"):
  print(-1)
else:
  print(max(ans))

print(*dp, sep = "\n")

# 動的計画法で解く
# 各商品ごとのパラメーターの値をP以上にするために必要な最小のコストを求める
# 3次元配列にして、dp[i][j][k] = i番目の商品まで見たときに、j個のパラメーターの値をk以上にするために必要な最小のコスト