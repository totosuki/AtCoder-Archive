r, g, b = input().split()
rgb = int(r + g + b)
if rgb % 4 == 0:
  print("YES")
else:
  print("NO")