V, T, S, D = map(int, input().split())
dist1 = V * T
dist2 = V * S
if dist1 <= D <= dist2:
  print("No")
else:
  print("Yes")