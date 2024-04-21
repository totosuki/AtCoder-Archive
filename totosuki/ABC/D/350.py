class UnionFind:
  def __init__(self, n):
    self.parent = list(range(n))
    self.rank = [0] * n
    self.size = [1] * n

  def find(self, x):
    if self.parent[x] == x:
      return x
    else:
      self.parent[x] = self.find(self.parent[x])
      return self.parent[x]

  def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    if rootX != rootY:
      if self.rank[rootX] < self.rank[rootY]:
        self.parent[rootX] = rootY
        self.size[rootY] += self.size[rootX]
      elif self.rank[rootX] > self.rank[rootY]:
        self.parent[rootY] = rootX
        self.size[rootX] += self.size[rootY]
      else:
        self.parent[rootY] = rootX
        self.rank[rootX] += 1
        self.size[rootX] += self.size[rootY]

  def getSize(self, x):
    return self.size[self.find(x)]

def solve():
  N, M = map(int, input().split())
  uf = UnionFind(N)
  for a, b in [map(int, input().split()) for _ in range(M)]:
    uf.union(a-1, b-1)

  maxOps = 0
  for i in range(N):
    root = uf.find(i)
    size = uf.size[root]
    maxOps += size - 1
  maxOps = maxOps // 2 - M
  return maxOps

print(solve())