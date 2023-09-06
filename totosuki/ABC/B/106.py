def f(n: int) -> int:
  x = 1
  cnt = 0
  while x*x <= n:
    if n % x == 0:
      cnt += 1
      if n/x != x:
        cnt += 1
    x += 1
  return cnt

N = int(input())
rslt = 0

for n in range(N+1):
  if n % 2 == 0: continue
  if f(n) == 8:
    rslt += 1

print(rslt)