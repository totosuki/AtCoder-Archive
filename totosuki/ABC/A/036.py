A, B = map(int, input().split())
if B % A:
  print(int((B / A) + 1))
else:
  print(int(B / A))