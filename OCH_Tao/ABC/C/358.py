import itertools
N,M = map(int,input().split())
ans = int("1"*M,2)
L = []
for i in range(N):
  S = input()
  S = S.replace("o","1")
  S = S.replace("x","0")
  L.append(int(S,2))
for i in range(1,N+1):
  P = itertools.permutations(L,i)
  for j in P:
    cnt = j[0]
    for k in j:
      cnt=cnt|k
    else:
      if ans==cnt:
        print(i)
        break
  else:
    continue
  break