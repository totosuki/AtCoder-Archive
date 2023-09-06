n, x = map(int, input().split())
if x > (n+1) / 2:
  print(n - x)
else:
  print(x - 1)