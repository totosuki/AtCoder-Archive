N = int(input())
A = list(map(int,input().split()))
L = []
for i in range(N):
  if A[i]!=i+1:
    L.append([min(i+1,A[i]),max(i+1,A[i])])
    x=A[i]
    A[i],A[x-1]=A[x-1],A[i]
print(len(L))
for i in L:
  print(*i)