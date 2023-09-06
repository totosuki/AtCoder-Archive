H, A = map(int, input().split())
if H % A:
  print(H // A + 1)
else:
  print(H // A)