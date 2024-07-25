# from math import perm
# from itertools import permutations
# from collections import Counter
# N,K = map(int,input().split())
# S = list(input())
# D = Counter(S)
# cnt = perm(N)
# for i in D.values():
#   cnt//=i
# X = set(["".join(i) for i in permutations(S,K) if "".join(i)=="".join(i)[::-1]])
# Y = set()
# for i in X:
#   ans = S.copy()
#   for j in list(i):
#     ans.remove(str(j))
#   for k in permutations([*ans,i],N-K+1):
#     Y.add("".join(k))
# print(cnt-len(Y))
from itertools import permutations
N,K = map(int,input().split())
S = list(input())
X = set(["".join(i) for i in permutations(S)])
Y = set(["".join(i) for i in permutations(S,K) if "".join(i)=="".join(i)[::-1]])
cnt = 0
for i in X:
  if all([j not in i for j in Y]):
    cnt+=1
print(cnt)