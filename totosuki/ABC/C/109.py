def GCD(a: int, b: int) -> int:
  if a < b:
    return GCD(b, a)
  else:
    if b == 0:
      return a
    else:
      return GCD(b, a % b)

N, X = map(int, input().split())
x = list(map(int, input().split()))

rslt = 0
for i in range(N):
  rslt = GCD(rslt, abs(X - x[i]))

print(rslt)