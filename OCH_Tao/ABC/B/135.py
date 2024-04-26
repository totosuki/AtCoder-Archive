from copy import deepcopy
N = int(input())
P = list(map(int,input().split()))
for i in range(N):
  for j in range(N):
    L = deepcopy(P)
    L[i],L[j]=L[j],L[i]
    if L==list(range(1,N+1)):
      print("YES")
      break
  else:
    continue
  break
else:
  print("NO")