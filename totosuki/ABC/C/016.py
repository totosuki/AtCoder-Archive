import sys; from collections import defaultdict
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, N+1):
  f_se = set(graph[i])
  ff_se = set()
  
  for f in f_se:
    ff_li = graph[f]
    for ff in ff_li:
      if (ff not in f_se) and (ff != i):
        ff_se.add(ff)
  
  print(len(ff_se))