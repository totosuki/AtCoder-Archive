class FenwickTree:
  def __init__(self, n):
    self._n = n
    self.data = [0] * n
  
  def add(self, id: int, x: int):
    """id は 0-indexed"""
    if 0 <= id < self._n:
      id += 1 # 0-indexed -> 1-indexed
      while id <= self._n:
        self.data[id - 1] += x # data を更新
        id += id & -id # id に LSB(id)を加算

  def sum(self, left: int, right: int) -> int:
    """
    左閉右開の半開区間 [l, r) の部分和を出力する\n
    left, right ともに 0-indexed
    """
    sm = 0 # sum
    if 0 <= left < right <= self._n:
      return self._sum(right) - self._sum(left)

  def _sum(self: int, right: int) -> int:
    sm = 0 # sum
    while right > 0:
      sm += self.data[right - 1]
      right -= right & -right # right から LSB(right) を減算
    return sm

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# set Fenwick Tree
ft = FenwickTree(n = N)
for i in range(N): ft.add(i, A[i])

for _ in range(Q):
  L, R = map(int, input().split())
  L, R = map(lambda x: x-1, [L, R])
  print(ft.sum(L, R+1))