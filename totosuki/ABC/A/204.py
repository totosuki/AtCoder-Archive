x, y = map(int, input().split())
if x == y:
  print(x)
else:
  for i in [0,1,2]:
    if i != x and i != y:
      print(i)