X, A, B = map(int, input().split())
if abs(X - A) < abs(X - B):
  print("A")
else:
  print("B")