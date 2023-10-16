from collections import defaultdict
from heapq import heappush, heappop, heapify

class QuasiMultiset:
  def __init__(self,deleteFlag=True):
    '''
    deleteFlag: 要素数が0となったkeyを辞書から削除するか
    '''
    self.len = 0
    self.f = defaultdict(int)
    self.pos = []
    self.neg = []
    self.deleteFlag = deleteFlag

  def _delete(self,key):
    if self.deleteFlag and self.f[key] == 0:
      del self.f[key]

  def add(self,x,key=None):
    '''
    x:追加する要素の値
    key:キー
    '''
    if key is None:
        key = x
    self.len += 1
    heappush(self.pos,(x,key))
    heappush(self.neg,(-x,key))
    self.f[key] += 1

  def popMax(self,returnKey=False):
    '''
    最大値とそのkey(optional)をpopする
    '''
    while True:
      x,key = heappop(self.neg)
      if self.f[key]:
        self.f[key] -= 1
        self.len -= 1
        self._delete(key)
        if returnKey:
          return -x,key
        else:
          return x

  def popMin(self,returnKey=False):
      '''
      最小値とそのkey(optional)をpopする
      '''
      while True:
          x,key = heappop(self.pos)
          if self.f[key]:
              self.f[key] -= 1
              self.len -= 1
              self._delete(key)
              if returnKey:
                  return x,key
              else:
                  return x

  def seachMax(self,returnKey=False):
      '''
      最大値とそのkey(optional)をreturnする
      '''
      while True:
          x,key = self.neg[0]
          if self.f[key]:
              if returnKey:
                  return -x,key
              else:
                  return -x
          else:
              heappop(self.neg)

  def seachMin(self,returnKey=False):
      '''
      最小値とそのkey(optional)をreturnする
      '''
      while True:
          x,key = self.pos[0]
          if self.f[key]:
              if returnKey:
                  return x,key
              else:
                  return x
          else:
              heappop(self.pos)

  def deleteKey(self,key):
      '''
      key:削除するkey
      '''
      self.f[key] -= 1
      self._delete(key)
      self.len -= 1

  def exist(self,key):
      if self.f.get(key) is None:
          return False
      else:
          return True

N = int(input())
slime = [list(map(int, input().split())) for _ in range(N)]
slime.sort(key = lambda x: x[0])
dict = defaultdict(int)
heap = QuasiMultiset()

for i in range(N):
  dict[slime[i][0]] = slime[i][1]
  heap.add(slime[i][0])

# 2倍にしたものか、次のslimeの大きさがどちらが大きいかで場合分け
# やっぱり大きさをheapqするしかない

cnt = 0

while len(heap.pos) > 0: # とりあえず無限ループ
  print(heap.pos)
  
  s = heap.popMin()
  c = dict[s]
  
  s = s * 2
  
  if c % 2 == 1:
    cnt += 1
  
  if c // 2 > 0:
    dict[s] += c // 2
    if dict[s] == 1:
      cnt += 1
      continue
    
    heap.add(s)

print(cnt)

# i = 0 # 最小のスライムのインデックス
# cnt = 0 # 残ったスライムの数

# while len(slime) > 0:
#   # print(slime)
  
#   s, c = heapq.heappop(slime)
#   if len(slime) > 0: # 二番目に小さいスライムがある場合
#     s2, c2 = heapq.heappop(slime)
#   else:
#     s2, c2 = -1, -1
  
#   if s == s2: # 二倍にしたやつと元々が同じ場合の処理
#     c = c + c2
#     new_c = s * 2
    
#     if c // 2 > 0:
#       heapq.heappush(slime, [new_c, c // 2])
    
#     if c % 2 == 1:
#       cnt += 1
#   else:
#     new_c = s * 2
    
#     if c // 2 > 0:
#       heapq.heappush(slime, [new_c, c // 2])
    
#     if c % 2 == 1:
#       cnt += 1
    
#     if s2 != -1: # 二番目に小さいスライムがない場合は何もしない
#       heapq.heappush(slime, [s2, c2])

# print(cnt)

# Sがスライムの大きさでCがスライムの数