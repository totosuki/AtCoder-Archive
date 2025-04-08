from decimal import Decimal, ROUND_DOWN
N = input()
if len(N) < 4:
  print(N)
else:
  print(int(Decimal(N).quantize(Decimal(f"1E{len(N)-3}"), ROUND_DOWN)))
