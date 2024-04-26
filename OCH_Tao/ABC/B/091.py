N = int(input())
S = []
for i in range(N):
  S.append(input())
M = int(input())
T = []
for i in range(M):
  T.append(input())
L = list(set(S)|set(T))
X = 0
for i in range(len(L)):
  cnt = 0
  cnt += S.count(L[i])
  cnt -= T.count(L[i])
  X = max(cnt,X)
print(X)