X, Y = map(int, input().split())

if X < Y:
  if Y - X > 2:
    print("No")
  else:
    print("Yes")
else:
  if X - Y > 3:
    print("No")
  else:
    print("Yes")