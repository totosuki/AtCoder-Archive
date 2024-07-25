from itertools import product
N,T = map(int,input().split())
S = list(map(bool,map(int,list(input()))))
X = list(map(int,input().split()))
L1 = []
L0 = []
cnt = 0
for i in range(N):
  if S[i]:
    L1.append([X[i],X[i]+T])
  else:
    L0.append([X[i],X[i]-T])
P = product(L1,L0)
for i in P:
  if max(i[0])<min(i[1]) or max(i[1])<min(i[0]):
    continue
  else:
    cnt+=1
print(cnt)