L = []
for i in range(5):
  L.append(int(input()))
K = int(input())
while len(L)>1:
  x = L.pop(0)
  for i in L:
    if i-x > K:
      print(":(")
      break
  else:
    continue
  break
else:
  print("Yay!")