import math
N = int(input())

for i in reversed(range(N+1)):
  x = math.sqrt(i)
  if x.is_integer():
    print(i)
    break