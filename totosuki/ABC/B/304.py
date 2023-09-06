import math
N = int(input())

if N < 10 ** 3:
  print(N)
elif N < 10 ** 4:
  print(math.floor(N / 10) * 10)
elif N < 10 ** 5:
  print(math.floor(N / 100) * 100)
elif N < 10 ** 6:
  print(math.floor(N / 1000) * 1000)
elif N < 10 ** 7:
  print(math.floor(N / 10000) * 10000)
elif N < 10 ** 8:
  print(math.floor(N / 100000) * 100000)
else:
  print(math.floor(N / 1000000) * 1000000)