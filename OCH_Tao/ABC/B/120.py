A,B,K = map(int,input().split())
L = []
for i in range(1,max(A,B)+1):
  if A%i==0 and B%i==0:
    L.append(i)
L.reverse()
print(L[K-1])