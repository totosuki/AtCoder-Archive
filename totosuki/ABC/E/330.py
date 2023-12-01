from collections import defaultdict
from sortedcontainers import SortedSet

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# set cnt_dict
cnt_dict = defaultdict(int)
for a in A: cnt_dict[a] += 1

# set SortedSet
sortedSet = SortedSet(iterable = [n for n in range(N+1) if cnt_dict[n] == 0])

for _ in range(Q):
  i, x = map(int, input().split())
  i -= 1
  before = A[i]
  A[i] = x
  
  cnt_dict[before] -= 1
  cnt_dict[x] += 1
  
  if cnt_dict[before] == 0:
    sortedSet.add(value = before)
  
  if cnt_dict[x] == 1:
    sortedSet.discard(value = x)
  
  print(sortedSet[0])