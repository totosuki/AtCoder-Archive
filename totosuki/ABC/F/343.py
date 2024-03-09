class SegmentTree:
  def __init__(self, n:int, op, e, v:list = None):
    self._n = n	 # 配列の長さ
    self._op = op # 演算（二項演算）
    self._e = e	 # 単位元
    self._log :int = (n - 1).bit_length() # 2 ** _log >= n となる最小の整数
    self._size:int = 2 ** self._log			 # 単位元が配列に入ったときの長さ
    self._data:list = [self._e()] * (2 * self._size) # セグメント木
    if v != None:
      # 葉に対象の列を格納
      for i in range(self._n):
        self._data[self._size + i] = v[i]
      # 葉に近い場所から順に更新
      for i in range(self._size-1, 0, -1): # (0, self._size-1] のため
        self._data[i] = self._merge(self._data[i << 1], self._data[i << 1 | 1])
  
  def set(self, p, x):
    """更新クエリ：配列[p] を x に更新"""
    if 0 <= p < self._n:
      p += self._size # 葉に移動
      self._data[p] = x
      # 関連する場所を更新
      while p:
        self._data[p >> 1] = self._merge(self._data[p], self._data[p ^ 1]) # p^1 == 2**0 を反転
        p >>= 1
    else:
      raise ValueError("p が 0 <= p < self._n ではありません。")
  
  def _merge(self, left, right):
    l1, l2, l1c, l2c = left
    r1, r2, r1c, r2c = right
    max_val = max(l1, r1) # 最大値は確実にこれ
    candidates = [l1, l2, r1, r2]
    candidates.remove(max_val)
    second_max = max(candidates)
    
    max_count = 0
    second_max_count = 0
    for val in [(l1, l1c), (l2, l2c), (r1, r1c), (r2, r2c)]:
      if val[0] == max_val:
        max_count += val[1]
      elif val[0] == second_max:
        second_max_count += val[1]
    
    return (max_val, second_max, max_count, second_max_count)
  
  def product(self, l, r):
    # 区間 [l, r) の2番目に大きい値の個数を取得
    if l >= r:
      return 0  # 無効な区間
    l += self._size
    r += self._size
    left_rslt = self._e()
    right_rslt = self._e()
    while l < r:
      if l & 1:
        left_rslt = self._merge(left_rslt, self._data[l])
        l += 1
      if r & 1:
        r -= 1
        right_rslt = self._merge(self._data[r], right_rslt)
      l >>= 1
      r >>= 1
    result = self._merge(left_rslt, right_rslt)
    return result[3]  # 2番目に大きい値の個数を返す

# 入力処理
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 単位元
def e(): return (float('-inf'), float('-inf'), 0, 0)  # 最大値、2番目に大きい値、最大値の個数、2番目に大きい値の個数

# セグメントツリーの初期化
st = SegmentTree(N, lambda x, y: x + y, e, [(a, float('-inf'), 1, 0) for a in A])

for i, a in enumerate(A):
  st.set(i, (a, 0, 1, 0))

# クエリ処理
for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    # タイプ1: 値の更新
    p, x = query[1], query[2]
    st.set(p - 1, (x, float('-inf'), 1, 0))
  else:
    # タイプ2: 2番目に大きい値の個数を出力
    l, r = query[1], query[2]
    print(st.product(l - 1, r))