from collections import defaultdict

N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
  A, B = map(int, input().split())
  G[A].append(str(B))
  G[B].append(str(A))

for k in range(1, N+1):
  text = f"{k}: " + "{" + ", ".join(G[k]) + "}"
  print(text)