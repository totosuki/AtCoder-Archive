W, H, N = map(int, input().split())
rslt = [[0, H], [0, W]]

for _ in range(N):
  x, y, a = map(int, input().split())
  if a == 1 and rslt[1][0] < x:
    rslt[1][0] = x
  elif a == 2 and rslt[1][1] > x:
    rslt[1][1] = x
  elif a == 3 and rslt[0][0] < y:
    rslt[0][0] = y
  elif a == 4 and rslt[0][1] > y:
    rslt[0][1] = y

if rslt[0][1] < rslt[0][0]:
  rslt[0][0] = rslt[0][1]
if rslt[1][1] < rslt[1][0]:
  rslt[1][0] = rslt[1][1]

area = (rslt[0][1]-rslt[0][0]) * (rslt[1][1]-rslt[1][0])
if area < 0:
  print(0)
else:
  print(area)