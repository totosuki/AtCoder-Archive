import itertools
L = []
for i in range(5):
  L.append(int(input()))
X = list(itertools.permutations(L))
rslt = []
for i in X:
  cnt = 0
  for j in range(5):
    cnt+=i[j]
    if j==4:
      break
    while cnt%10>0:
      cnt+=1
  rslt.append(cnt)
print(min(rslt))