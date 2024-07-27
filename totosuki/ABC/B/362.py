import math

xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

def distance_squared(x1, y1, x2, y2):
  return (x1 - x2) ** 2 + (y1 - y2) ** 2

ab2 = distance_squared(xa, ya, xb, yb)
bc2 = distance_squared(xb, yb, xc, yc)
ca2 = distance_squared(xc, yc, xa, ya)

if ab2 + bc2 == ca2 or ab2 + ca2 == bc2 or bc2 + ca2 == ab2:
  print("Yes")
else:
  print("No")