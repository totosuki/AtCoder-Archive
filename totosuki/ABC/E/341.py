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

N, Q = map(int, input().split())
S = list(input())

bad = FenwickTree(N)

for i in range(N-1):
  if S[i] == S[i+1]:
    bad.add(i, 1)

for _ in range(Q):
  q, l, r = map(int, input().split())
  l, r = l-1, r # lを0-indexedに、rはそのままで
  if q == 1: # L, Rを入れ替える
    
    # lが右端の場合スキップ
    if l > 0 and bad.data[l-1] == 1:
      bad.add(l-1, -1)
    elif l > 0 and bad.data[l-1] == 0:
      bad.add(l-1, 1)
      
    # rが右端の場合スキップ
    if r < N and bad.data[r-1] == 1:
      bad.add(r-1, -1)
    elif r < N and bad.data[r-1] == 0:
      bad.add(r-1, 1)
  else:
    if l+1 == r: # lとrが同じ場合、l+1とrが等しくなる
      print("Yes")
    elif bad.sum(l, r) == 0:
      print("Yes")
    else:
      print("No")
  # print(f"bad.data: {bad.data}")


# 考察
# 結局変わる場所はL, Rの部分のみ。
# L, Rが変わる際に、変わる切れ目が良い文字列なら、悪くなり、悪い文字列なら、良い文字列になる。

# 切れ目の部分が良いか悪いかをメモしとけばいい？
# 切れ目を1-indexで管理して、文字は0-indexで管理すると良さげ。
# 切れ目の左側の文字列との違いは、その番号。右側の文字列との違いは、その番号+1。

# 難しそうなのは、区間L, Rで確認する際に、切れ目があるかどうかを確認すること。

# フェニック木を使えば行ける？？？

# badが1の場合は、悪い文字列！！