import heapq

N = int(input())
edges = [[] for _ in range(N+1)]

for i in range(1, N):
  a, b, x = map(int, input().split())
  edges[i].append((i+1, a))  # ステージiからステージi+1への遷移
  edges[i].append((x, b))    # ステージiからステージX[i]への遷移

def dijkstra(start):
  dist = [float('inf')] * (N+1)
  dist[start] = 0
  queue = [(0, start)]  # (距離, 頂点)
  while queue:
    d, v = heapq.heappop(queue)
    if dist[v] < d:
      continue
    for to, cost in edges[v]:
      if dist[to] > dist[v] + cost:
        dist[to] = dist[v] + cost
        heapq.heappush(queue, (dist[to], to))
  return dist

distances = dijkstra(1)
print(distances[N])