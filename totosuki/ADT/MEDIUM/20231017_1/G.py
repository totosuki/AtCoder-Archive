from itertools import permutations
from math import factorial

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [tuple(input().split("_")) for _ in range(M)]

if N == 1:
  under = 0
else:
  under = 16 - len("".join(S))

one_under = under - N
answer = -1

for perm in permutations(S):
  s = "_".join(perm)
  count = T.count(perm)
  if factorial(one_under) > count:
    answer = perm
    break