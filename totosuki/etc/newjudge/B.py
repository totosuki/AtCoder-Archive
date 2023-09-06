from decimal import Decimal, ROUND_HALF_UP

X, K = map(int, input().split())

def my_round(N, power: int):
  adjust = 1 if N >=0 else -1
  shift = 10 ** (power-1)
  N = abs(N * shift)
  return (int(N + 0.5) / shift) * adjust

for i in range(K):
  X = Decimal(str(X)).quantize(Decimal(str(f"1E{i+1}")), rounding = ROUND_HALF_UP)

print(int(X))