X = int(input())
L = []
for i in range(2,10):
  for j in range(1,32):
    L.append(j**i)
L = list(set(L))
L = [i for i in L if i<=X]
print(max(L))