from sortedcontainers import SortedSet

class FenwickTree:
  def __init__(self, n):
    self._n = n
    self.data = [0] * n
  
  def add(self, id: int, x: int):
    """idは 0-indexed"""
    if 0 <= id < self._n:
      id += 1 # 0-indexed -> 1-indexed
      while id <= self._n:
        self.data[id - 1] += x # data を更新
        id += id & -id # id に LSB(id) を加算
    else:
      raise ValueError("id が  0 <= id < self._n  ではありません。")
  
  def sum(self, left: int, right: int) -> int:
    """
    左閉右開の半開区間 [l, r) の部分和を出力する\n
    left, right ともに 0-indexed
    """
    sm = 0 # sum
    if 0 <= left < right <= self._n:
      return self._sum(right) - self._sum(left)
    else:
      raise ValueError("left, right が  0 <= left < right <= self._n  ではありません。")
  
  def _sum(self, right : int) -> int:
    sm = 0 # sum
    while right > 0:
      sm += self.data[right - 1]
      right -= right & -right # right から LSB(right) を減算
    return sm

N = int(input())
H = list(map(int, input().split()))

S = SortedSet([])
fw = FenwickTree(N)
ans = []

for i in range(N):
  S.add(H[i])
  mx = S.pop()
  if mx == H[i]:
    S.add(mx)
    ans.append(mx * (i + 1))
    sm = fw.sum(0, i + 1)
    fw.add(i, mx-sm)
  else:
    S.add(mx)
    fw.add(i, mx)
    ans.append(fw.sum(0, i + 1))
  

print(*ans)