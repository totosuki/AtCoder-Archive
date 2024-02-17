N = int(input())
L = [2,1]
for i in range(1,N):
  L.append(L[i-1]+L[i])
print(L[-1])