N, M = map(int, input().split())
pairs = [[False] * N for _ in range(N)]

for _ in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  pairs[u][v] = True
  pairs[v][u] = True

rslt = 0

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      if pairs[i][j] and pairs[j][k] and pairs[k][i]:
        rslt += 1

print(rslt)

# graphs = [list(map(int, input().split())) for _ in range(M)]

# pairs = []
# for graph in graphs:
#   if not pairs:
#     pairs.append(graph)
#   else:
#     for i in range(len(pairs)):
#       if graph[0] in pairs[i] or graph[1] in pairs[i]:
#         pairs[i].append(graph[0])
#         pairs[i].append(graph[1])
#         print(pairs)
