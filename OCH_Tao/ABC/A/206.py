import math
N = int(input())
x = math.floor(N*1.08)
if x < 206:
  print("Yay!")
elif x == 206:
  print("so-so")
else:
  print(":(")