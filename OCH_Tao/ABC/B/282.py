from itertools import combinations
N,M = map(int,input().split())
L = []
for i in range(N):
  S = input()
  L.append(int(S.replace("o","1").replace("x","0"),base=2))
cnt = 0
for i in combinations(L,2):
  if i[0]|i[1]==int("1"*M,base=2):
    cnt+=1
print(cnt)