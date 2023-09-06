A, B = map(int, input().split())
if A > B:
  print(A + A - 1)
elif A < B:
  print(B + B - 1)
else:
  print(A + B)