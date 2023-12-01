import sys
input = sys.stdin.buffer.readline

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
        self._data[i] = self._op(self._data[i << 1], self._data[i << 1 | 1])
  
  def set(self, p, x):
    """更新クエリ：配列[p] を x に更新"""
    if 0 <= p < self._n:
      p += self._size # 葉に移動
      self._data[p] = x
      # 関連する場所を更新
      while p:
        self._data[p >> 1] = self._op(self._data[p], self._data[p ^ 1]) # p^1 == 2**0 を反転
        p >>= 1
    else:
      raise ValueError("p が 0 <= p < self._n ではありません。")
  
  def product(self, l, r):
    """
    取得クエリ：区間 [l, r) の総積を取得\n
    l == r の場合は単位元を返す
    """
    if 0 == l == r == 0:
      raise ValueError("l, r が 0 == l == r == 0 です。")
    if 0 <= l <= r <= self._n:
      left_rslt, right_rslt = self._e(), self._e() # 左右の結果を初期化
      l += self._size
      r += self._size
      # 未計算の区間が無くなるまで
      while l < r:
        # l が右子ノードなら
        if l & 1:
          left_rslt = self._op(left_rslt, self._data[l])
          l += 1 # 親ノードを右隣に変更
        # (r-1 が左子ノードなら) == (r が右子ノードなら)
        if r & 1:
          right_rslt = self._op(self._data[r-1], right_rslt) # 交換法則が常に成り立たない為
          r -= 1 # 親ノードを左隣に変更
        # 親に移動
        l >>= 1
        r >>= 1
      return self._op(left_rslt, right_rslt)
    else:
      raise ValueError("l, r が 0 <= l <= r <= self._n ではありません。")
  
  def all_product(self):
    """全要素の総積を取得"""
    return self._data[1]
  
  def get(self, p):
    """セグメント木の配列[p]を取得"""
    if 0 <= p < self._n:
      return self._data[p + self._size]
    else:
      raise ValueError("p が 0 <= p < self._n ではありません。")
  
  def max_right(self, l, f):
    """
    右探索クエリ：f(op(left,right)) = True となる最大の right を取得\n
    f(self._e()) = True かつ 0 <= left <= self._n
    """
    if not f(self._e()): raise ValueError("f(self._e()) が False になってます。")
    if 0 <= l < self._n:
      right = l + self._size # 葉に移動
      rslt = self._e()
      while True:
        while right % 2 == 0: right >>= 1 # 右ノードになるまで
        if not f(self._op(rslt, self._data[right])):
          # ノード right が覆う範囲を二分探索
          while right < self._size:
            right <<= 1 # 左子ノードに移動
            if f(self._op(rslt, self._data[right])):
              rslt = self._op(rslt, self._data[right])
              right += 1 # f = True ならば右隣のノードに移動
          return right - self._size # right は境界の False 側で終わる
        else:
          rslt = self._op(rslt, self._data[right])
          right += 1 # f = True ならば右隣のノードに移動
          if right & -right == right: return self._n # f(op(l, n)) が確定
    elif l == self._n: return self._n
    else: raise ValueError("l が 0 <= l <= self._n ではありません。")
  
  def min_left(self, r, f):
    """
    左探索クエリ：f(op(left,right)) = True となる最小の left を取得\n
    f(self._e()) = True かつ 0 <= right <= self._n
    """
    if not f(self._e()): raise ValueError("f(self._e()) が False になってます。")
    if 0 < r <= self._n:
      left = r + self._size
      rslt = self._e()
      while True:
        left -= 1 # 右開区間 [left, r) のため先にデクリメント
        while left > 1 and left % 2: left >>= 1 # left が左子ノードになるまで
        if not f(self._op(self._data[left], rslt)):
          # ノード left が覆う範囲を二分探索
          while left < self._size:
            left = 2 * left + 1 # 右子ノードに移動
            if f(self._op(self._data[left], rslt)):
              rslt = self._op(self._data[left], rslt)
              left -= 1 # f = True ならば左隣のノードに移動
          return left + 1 - self._size # left は境界の False 側で終わる
        else:
          rslt = self._op(self._data[left], rslt)
          if left & -left == left: return 0 # 各層の左端に来たら left = 0 となる
    elif r == 0: return 0
    else: raise ValueError("r が 0 <= r <= self._n ではありません。")

def op(x, y):
  return max(x, y)

def e():
  return -1

def main():
  N, Q = map(int, input().split())
  A = list(map(int, input().split()))
  seg = SegmentTree(N, op, e, A)
  for _ in range(Q):
    T, X, Y = map(int, input().split())
    X -= 1 # 0-indexed
    if T == 1:
      seg.set(X, Y)
    if T == 2:
      print(seg.product(X, Y))
    if T == 3:
      f = lambda x: x < Y
      print(seg.max_right(X, f) + 1)

main()