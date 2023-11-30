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
    取得クエリ：区間 [l, r) の総積を取得
    l == r の場合は単位元を返す
    """
    if 0 <= l < r <= self._n:
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
      raise ValueError("l, r が 0 <= l < r <= self._n ではありません。")
  
  def all_product(self):
    """全要素の総積を取得"""
    return self._data[1]
  
  def get(self, p):
    """セグメント木の配列[p]を取得"""
    if 0 <= p < self._n:
      return self._data[p + self._size]
    else:
      raise ValueError("p が 0 <= p < self._n ではありません。")

def op(x, y):
  return x ^ y

def e():
  return 0

def main():
  N, Q = map(int, input().split())
  A = list(map(int, input().split()))
  seg = SegmentTree(n = N, op = op, e = e, v = A)
  for _ in range(Q):
    T, X, Y = map(int, input().split())
    if T == 1:
      seg.set(X - 1, seg.get(X - 1) ^ Y)
    if T == 2:
      print(seg.product(l = X-1, r = Y))

main()
