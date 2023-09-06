import math
a, b = input().split()
rslt = int(a+b)

if math.sqrt(rslt).is_integer():
  print("Yes")
else:
  print("No")