M = int(input())
L = []
for i in range(10,-1,-1):
  while M>=3**i:
    L.append(i)
    M-=3**i
print(len(L))
print(*L)