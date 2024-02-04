from collections import deque

N = int(input())
A = list(map(int, input().split()))

def check(k):
  if k == 1:
    return True
  
  B = A.copy()
  i = 0
  next = 1
  isup = True
  
  while True:
    if isup:
      if B[i] >= next:
        next += 1
      else:
        next = B[i] + 1
    if not isup:
      if B[i] >= next:
        next -= 1
      else:
        next = B[i] + 1
        isup = True
    # kまで来たら isup = False
    if next == k:
      isup = False
    
    if len(B) - 1 == i:
      return False
    if not isup and next == 1:
      return True
    # インクリメント
    i += 1

l = 0
r = N + 5
while r - l > 1:
  mid = (l + r) // 2
  if check(mid):
    l = mid
  else:
    r = mid

print(l)