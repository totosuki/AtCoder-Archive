from math import sqrt,trunc
A,B = input().split()
X = int(A+B)
if trunc(sqrt(X))**2 == X:
  print("Yes")
else:
  print("No")