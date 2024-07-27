import heapq
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
U = []
V = []
B = []
for _ in range(M):
  u, v, b = map(int, input().split())
  u -= 1
  v -= 1
  U.append(u)
  V.append(v)
  B.append(b)

graph = defaultdict(list)
for u, v, b in zip(U, V, B):
  graph[u].append((v, b))
  graph[v].append((u, b))

q = []
heapq.heappush(q, (A[0], 0))

dist = [float('inf')] * N
dist[0] = A[0]

while q:
  current_weight, u = heapq.heappop(q)
  
  if current_weight > dist[u]:
    continue
  
  for v, b in graph[u]:
    new_weight = current_weight + A[v] + b
    if new_weight < dist[v]:
      dist[v] = new_weight
      heapq.heappush(q, (new_weight, v))

print(*dist[1:])
