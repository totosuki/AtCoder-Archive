from math import sqrt

N = int(input())

XY = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
  ans = (i, 0)
  for j in range(N):
    if i == j:
      continue
    dist = sqrt((XY[i][0] - XY[j][0])**2 + (XY[i][1] - XY[j][1])**2)
    if dist > ans[1]:
      ans = (j, dist)
  print(ans[0]+1)
