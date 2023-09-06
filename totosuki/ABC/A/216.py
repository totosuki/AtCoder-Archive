X, Y = map(int, input().split("."))
if Y <= 2:
  print(str(X) + "-")
elif Y <= 6:
  print(X)
else:
  print(str(X) + "+")