from decimal import Decimal,ROUND_HALF_UP
A,B = map(int,input().split())
print(Decimal(B/A).quantize(Decimal("0.001"),ROUND_HALF_UP))