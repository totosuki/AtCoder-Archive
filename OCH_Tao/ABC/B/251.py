from itertools import combinations
N,W = map(int,input().split())
A = list(map(int,input().split()))
S = set()
for i in range(1,4):
  C = combinations(A,i)
  for j in C:
    X = sum(j)
    if X<=W:
      S.add(X)
print(len(S))