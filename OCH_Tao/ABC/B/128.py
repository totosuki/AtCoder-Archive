N = int(input())
X = []
L = set()
for i in range(N):
  S,P = input().split()
  L.add(S)
  X.append([S,int(P),i+1])
L = sorted(list(L))
for i in L:
  l = [j for j in X if j[0]==i]
  l = sorted(l,key=lambda x:x[1],reverse=True)
  for k in l:
    print(k[2])