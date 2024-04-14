from pandas import DataFrame

N = int(input())
S = [0] + list(map(int, input()))
C = [0] + list(map(int, input().split()))

# DP初期化
dp00 = [float("inf")] * (N+1)
dp01 = [float("inf")] * (N+1)
dp10 = [float("inf")] * (N+1)
dp11 = [float("inf")] * (N+1)
dp00[0] = 0
# dp01[0] = 0
dp10[0] = 0
# dp11[0] = 0

# DP
for i in range(1, N+1):
  if S[i] == 0:
    dp00[i] = dp10[i-1]
    dp10[i] = dp00[i-1] + C[i]
    if i == 1:
      dp01[i] = float("inf")
      dp11[i] = float("inf")
    else:
      dp01[i] = min(dp00[i-1], dp11[i-1])
      dp11[i] = min(dp01[i-1] + C[i], dp10[i-1] + C[i])
  else:
    dp00[i] = dp10[i-1] + C[i]
    dp10[i] = dp00[i-1]
    if i == 1:
      dp01[i] = float("inf")
      dp11[i] = float("inf")
    else:
      dp01[i] = min(dp00[i-1] + C[i], dp11[i-1] + C[i])
      dp11[i] = min(dp01[i-1], dp10[i-1])

print(min(dp01[-1], dp11[-1]))

# 問題整理
# 0,1を交互に並べる
# 一つだけ0,0や1,1が有る必要がある
# 値を入れ替えるにはコストがかかる

# 方針
# 動的計画法を使って考えたい
# dp00 = i番目が0の時の最小コスト(良い文字列まだ)
# dp01 = i番目が0の時の最小コスト(良い文字列あり)
# dp10 = i番目が1の時の最小コスト(良い文字列まだ)
# dp11 = i番目が1の時の最小コスト(良い文字列あり)

# i番目が0の時
# dp00[i] = dp10[i-1]
# dp01[i] = min(dp00[i-1], dp11[i-1])
# dp10[i] = dp00[i-1] + C[i]
# dp11[i] = min(dp01[i-1] + C[i], dp10[i-1] + C[i])

# i番目が1の時
# dp00[i] = dp10[i-1] + C[i]
# dp01[i] = min(dp00[i-1] + C[i], dp11[i-1] + C[i])
# dp10[i] = dp00[i-1]
# dp11[i] = min(dp01[i-1], dp10[i-1])