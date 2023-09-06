SX, SY, GX, GY = map(int, input().split())
distX = abs(GX - SX)
step = distX / (SY + GY)
min_x = min(SX, GX)
if min_x == SX:
  rslt = SX + step * SY
else:
  rslt = GX + step * GY
print(rslt)