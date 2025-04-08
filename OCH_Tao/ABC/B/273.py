from decimal import Decimal,ROUND_HALF_UP
X,K = map(int,input().split())
for i in range(K):
  X = int(Decimal(X).quantize(Decimal(f"1E{i+1}"),ROUND_HALF_UP))
print(X)