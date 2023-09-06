from itertools import permutations
from collections import defaultdict

import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
rslt = -1
graph = defaultdict(set)
length_dict = defaultdict(int)

# make graph
for _ in range(M):
  A, B, C = map(int, input().split())
  graph[A].add(B)
  graph[B].add(A)
  length_dict[(A, B)] = C
  length_dict[(B, A)] = C

# serch max length
for pettern in permutations(range(1, N+1), N):
  length = 0
  now_pos = pettern[0]
  for i in range(1, N):
    if pettern[i] in graph[now_pos]:
      length += length_dict[(now_pos, pettern[i])]
      now_pos = pettern[i]
    else:
      break
  
  if rslt < length:
    rslt = length

print(rslt)
