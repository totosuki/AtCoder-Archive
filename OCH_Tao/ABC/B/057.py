N,M = map(int,input().split())
S = []
for i in range(N):
  S.append(list(map(int,input().split())))
C = []
for i in range(M):
  C.append(list(map(int,input().split())))
for i in range(N):
  l = []
  for j in range(M):
    l.append(abs(S[i][0]-C[j][0])+abs(S[i][1]-C[j][1]))
  else:
    print(l.index(min(l))+1)