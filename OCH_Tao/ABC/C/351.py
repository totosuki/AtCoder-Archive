N = int(input())
A = list(map(int,input().split()))
L = []
for i in range(N):
  L.append(A[i])
  while len(L)>1:
    if L[-2]!=L[-1]:
      break
    else:
      X = L.pop()
      L.pop()
      L.append(X+1)
print(len(L))