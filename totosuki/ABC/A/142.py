import math
N = int(input())
odd = math.ceil(N / 2)
even = math.ceil(N/ 2) - 1
if N % 2 == 0:
  print(0.5)
else:
  print(odd / N)