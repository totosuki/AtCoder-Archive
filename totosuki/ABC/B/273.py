from decimal import Decimal, ROUND_HALF_UP
X, K = map(int, input().split())
for i in range(K):
  place = "1E" + str(i+1)
  X = int(Decimal(X).quantize(Decimal(place), rounding = ROUND_HALF_UP))
print(X)