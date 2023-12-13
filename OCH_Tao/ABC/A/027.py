L = input().split()
if L.count(L[0]) == 3:
  print(L[0])
elif L.count(L[0]) == 1:
  print(L[0])
else:
  if L[0] == L[1]:
    print(L[2])
  else:
    print(L[1])