S = list(map(lambda x:bool(int(x)),list(input())))
T = [(0,6),(0,3),(0,1,7),(0,4),(0,2,8),(0,5),(0,9)]
X = [any([S[j] for j in i]) for i in T]
for i in range(5):
  for j in range(i+2,7):
    if X[i] and X[j] and not all(X[i+1:j]):
      print("Yes")
      break
  else:
    continue
  break
else:
  print("No")