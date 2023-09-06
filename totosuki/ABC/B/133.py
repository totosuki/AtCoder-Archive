import math
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N):
  for j in range(i+1, N):
    rslt = 0
    for d in range(D):
      rslt += (X[i][d] - X[j][d]) ** 2
    rslt = math.sqrt(rslt)
    if rslt.is_integer():
      cnt += 1

print(cnt)