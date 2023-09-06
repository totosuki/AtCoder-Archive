import math
X, Y = map(int, input().split())
if X < Y:
  print(math.ceil((Y-X) / 10))
else:
  print(0)