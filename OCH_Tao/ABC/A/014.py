A = int(input())
B = int(input())
if A % B == 0:
  print(0)
else:
  x = B - (A % B)
  print(x)