L = list(map(int,input().split()))
K = int(input())
L.sort(reverse=True)
for i in range(K):
  L[0]*=2
print(sum(L))