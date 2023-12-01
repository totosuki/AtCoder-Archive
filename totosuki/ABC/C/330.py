from math import isqrt

D = int(input())
sqrt_d = isqrt(D)
rslt = 1 << 60

for x in range(1, sqrt_d + 1):
  y = isqrt(D - x ** 2)
  y2 = y + 1
  z = abs(x ** 2 + y ** 2 - D)
  rslt = min(rslt, z)
  z = abs(x ** 2 + y2 ** 2 - D)
  rslt = min(rslt, z)

print(rslt)