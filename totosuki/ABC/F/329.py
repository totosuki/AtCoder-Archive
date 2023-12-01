N, Q = map(int, input().split())
C = list(map(int, input().split()))

hako = [set() for _ in range(N+1)]
for i in range(1, N+1):
  hako[i].add(C[i-1])

for _ in range(Q):
  a, b = map(int, input().split()) # aからbに移動して残りを求める
  if len(hako[a]) > len(hako[b]):
    for c in hako[b]:
      hako[a].add(c)
    hako[b] = hako[a]
    hako[a] = set()
  else:
    for c in hako[a]:
      hako[b].add(c)
    hako[a] = set()
  print(len(hako[b]))