W, A, B = map(int, input().split())
dist = abs(A-B)
rslt = dist - W

if rslt <= 0:
  print(0)
else:
  print(rslt)