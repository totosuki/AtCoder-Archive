N = int(input())
W = [input()]
for i in range(N-1):
  X = input()
  if W[-1][-1]==X[0] and X not in W:
    W.append(X)
  else:
    print("No")
    break
else:
  print("Yes")