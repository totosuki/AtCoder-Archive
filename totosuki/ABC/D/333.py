from collections import defaultdict, deque

def make_graph(N):
  graph = defaultdict(list)
  for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  return graph

def solve(N, graph):
  visited = [False] * (N+1)
  visited[1] = True
  rslt = []
  for node in graph[1]:
    cnt = 0
    q = deque([node])
    visited[node] = True
    while q:
      cnt += 1
      now = q.pop()
      next = graph[now]
      for n in next:
        if not visited[n]:
          visited[n] = True
          q.append(n)
    rslt.append(cnt)
  mx = max(rslt)
  sm = sum(rslt)
  print(sm - mx + 1)

def main():
  N = int(input())
  graph = make_graph(N)
  solve(N, graph)


main()
