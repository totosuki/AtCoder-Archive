def make_divisors(n):
  lower_divisors , upper_divisors = [], []
  i = 1
  while i*i <= n:
    if n % i == 0:
      lower_divisors.append(i)
      if i != n // i:
        upper_divisors.append(n//i)
    i += 1
  return lower_divisors + upper_divisors[::-1]

from bisect import bisect_left, bisect_right
from math import factorial

N = int(input())
A = list(map(int, input().split()))
A.sort()
square = []
for i in range(451):
  if i == 0:
    square.append([0, [0]])
    continue
  
  fact = make_divisors(i)
  square.append([i**2, fact])

cnt = 0

for i in range(451):
  nsq = square[i][0] # 平方数
  for x in square[i][1]: # 平方数の約数がAにあるか二分探索
    fid_l = bisect_left(A, x)
    if fid_l == N: continue # はみ出していたら次へ
    if A[fid_l] != x: continue # なければ次へ
    fid_r = bisect_right(A, x)
    
    if x == 0: # 0の場合すべてが対象になる
      for i in range(N):
        if A[i] == 0:
          cnt += N - (i + 1)
      continue
    
    tar = nsq // x
    sid_l = bisect_left(A, tar)
    
    if sid_l == N: continue # はみ出していたら次へ
    if A[sid_l] != tar: continue # なければ次へ
    sid_r = bisect_right(A, tar)
    
    if tar == x:
      if fid_r - fid_l > 1: # 2個以上ある場合
        print(nsq, x, tar, cnt)
        cnt += factorial((fid_r - fid_l) - 1)
    else:
      print(nsq, x, tar, cnt)
      cnt += (fid_r - fid_l) * (sid_r - sid_l)

print(cnt)

# 平方数はだいたい2 * 10**5 までだと450個くらい
# ソートしても良さそう
# 先に平方数を列挙しておく
# 平方数になる組み合わせは、平方数の約数の組み合わせのみになる。
# なので、素因数分解して、その数を列挙しておく
# あとは、それぞれの数に対して、Aに二分探索してあるか調べる
# データ構造は、[[平方数, [その平方数の約数列挙]]] とする