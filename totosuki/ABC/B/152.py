a, b = input().split()
ab = a * int(b)
ba = b * int(a)
if ab < ba:
  print(ab)
else:
  print(ba)