from decimal import Decimal,ROUND_HALF_UP
X = Decimal(input())
print(X.quantize(Decimal("0"),ROUND_HALF_UP))