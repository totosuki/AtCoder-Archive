N, M = map(int, input().split())
rslt = [[0]*N for _ in range(N)]
for _ in range(M):
  a, b = map(int, input().split())
  rslt[a-1][b-1] += 1
  rslt[b-1][a-1] += 1
for row in range(N):
  cnt = 0
  for col in range(N):
    cnt += rslt[row][col]
  print(cnt)