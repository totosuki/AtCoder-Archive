N = int(input())
S = []
for i in range(N):
  S.append(input())
S.reverse()
X=max(map(len,S))
for i in range(N):
  if len(S[i])<X:
    S[i]+="*"*(X-len(S[i]))
for i in range(X):
  print("".join([j[i] for j in S]).rstrip("*"))