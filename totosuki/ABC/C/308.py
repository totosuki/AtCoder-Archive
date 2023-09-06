from decimal import Decimal

N = int(input())
rslt = []

for i in range(1, N+1):
  A, B = map(Decimal, input().split())
  tmp = Decimal(Decimal(A) / (A+B))
  
  rslt.append([tmp, i])

rslt.sort(key = lambda x: (-x[0], x[1]))

for r in rslt:
  print(r[1], end = " ")
