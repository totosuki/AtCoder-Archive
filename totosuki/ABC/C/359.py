from math import ceil

sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

dx = abs(sx - tx)
dy = abs(sy - ty)

if dx <= dy:
  ans = dx + (dy - dx)
else:
  ans = dy
  dx = dx - dy
  if sy % 2 == 0 and sx % 2 == 1 and sx > tx: 
    dx -= 1
  elif sy % 2 == 1 and sx % 2 == 0 and sx > tx:
    dx -= 1
  elif sy % 2 == 0 and sx % 2 == 0 and sx < tx:
    dx -= 1
  elif sy % 2 == 1 and sx % 2 == 1 and sx < tx:
    dx -= 1
  ans += ceil(dx / 2)

print(ans)