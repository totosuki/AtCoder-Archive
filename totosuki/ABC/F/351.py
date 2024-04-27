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
A = list(map(int, input().split()))

# 座標圧縮
sorted_A = sorted(set(A))
index = {sorted_A[i]: i for i in range(len(sorted_A))}

ft = FenwickTree(N)
cnt = FenwickTree(N)

result = 0
for i in range(N):
  ai = A[i]
  # aiより小さい要素の合計を取得
  pos = index[ai]
  total = ft.sum(0, pos+1)
  total_cnt = cnt.sum(0, pos+1)
  result += max(ai * total_cnt - total, 0)
  # 現在の要素を追加
  ft.add(pos, ai)
  cnt.add(pos, 1)
  
  # print(f"{i} ai: {ai}, pos: {pos}, total: {total}, result: {result}")

print(result)

# 前の要素で自分より小さい値のみを引いた合計を求めるということ