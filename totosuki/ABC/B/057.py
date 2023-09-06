N, M = map(int, input().split())
s_pos = [list(map(int, input().split())) for _ in range(N)]
c_pos = [list(map(int, input().split())) for _ in range(M)]

for i in range(N):
  rslt = []
  for j in range(M):
    x_dist = abs(s_pos[i][0] - c_pos[j][0])
    y_dist = abs(s_pos[i][1] - c_pos[j][1])
    rslt.append(x_dist + y_dist)
  min_dist = min(rslt)
  min_id = rslt.index(min_dist)
  print(min_id + 1)