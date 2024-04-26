N = int(input())
L = []
for i in range(1,N+1):
  if i%3==0:
    L.append("x")
  else:
    L.append("o")
print("".join(L))