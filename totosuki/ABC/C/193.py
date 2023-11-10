from math import isqrt

N = int(input())
lim = isqrt(N)

log = set()
cnt = 0
a = 2
while a <= isqrt(N): # a**2 <= Nまで
  b = 2
  while a**b <= N:
    if a**b not in log:
      log.add(a**b)
      cnt += 1
    b += 1
  a += 1

print(N - len(log))