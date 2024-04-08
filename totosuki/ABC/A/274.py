from decimal import Decimal, ROUND_HALF_UP

A, B = map(int, input().split())
ans = Decimal(B / A)
print(ans.quantize(Decimal("0.000"), rounding = ROUND_HALF_UP))