# from heapq import heapify, heappop, heappush

from collections import defaultdict

class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x

  def size(self, x):
    return -self.parents[self.find(x)]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    group_members = defaultdict(list)
    for member in range(self.n):
      group_members[self.find(member)].append(member)
    return group_members

  def __str__(self):
    return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def main():
  N, M, K = map(int, input().split())
  uf = UnionFind(N)

  edges = []

  for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((w, u, v))

  # 重みが小さい順に辺をソート
  edges.sort()

  cost = 0

  for edge in edges:
    w, u, v = edge
    # 頂点がつながっていなければ
    if not uf.same(u, v):
      cost =  cost + w# 重みを足し
      uf.union(u, v) # 頂点同士をつなげる

  print(cost)

main()

# def return_graph(N, M):
#   graph = defaultdict(list)
#   for _ in range(M):
#     u, v, w = map(int, input().split())
#     u -= 1
#     v -= 1
#     graph[u].append((v, w))
#     graph[v].append((u, w))
#   return graph

# def solve(graph, N, K):
#   used = [0] * N
#   que = [(w, v) for v, w in graph[0]]
#   used[0] = 1
#   heapify(que)
  
#   ans = 0
#   while que:
#     w, v = heappop(que)
#     if used[v]: continue
#     used[v] = 1
#     ans = (ans + w) % K
#     for v, w in graph[v]:
#       if used[v]:
#         continue
#       heappush(que, (w, v))
#   return ans

# def main():
#   N, M, K = map(int, input().split())
#   graph = return_graph(N, M)
#   print(solve(graph, N, K))

# main()