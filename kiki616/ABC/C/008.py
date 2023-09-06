# import math

# N = int(input())
# C = []
# cnt = 0
# n_ = math.factorial(N)
# print(n_)

# for i in range(N):
#     c = int(input())
#     count = 0
#     for j in C:
#         if c % j:
#             count = count+1

#     if count % 2 == 0:
#         cnt = cnt + 1
#     C.append(c)

import sys, itertools, math
input = sys.stdin.buffer.readline

N = int(input())
C = [int(input()) for _ in range(N)]
rslt = []

for perm in itertools.permutations(C):
  status = [False] * N
  for i in range(N-1):
    a = perm[i]
    for j in range(i+1, N):
      if perm[j] % a == 0:
        status[j] = not status[j]
  rslt.append(status)

rslt = [r for i in range(math.factorial(N)) for r in rslt[i]]

print(rslt.count(False) / math.factorial(N))