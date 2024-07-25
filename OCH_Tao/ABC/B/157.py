A = []
for i in range(3):
  A.append(list(map(int,input().split())))
N = int(input())
B = []
for i in range(N):
  B.append(int(input()))
X = [[j in B for j in i] for i in A]
for i in X:
  if all(i):
    print("Yes")
    break
else:
  for i in range(3):
    if X[0][i] and X[1][i] and X[2][i]:
      print("Yes")
      break
  else:
    if (X[0][0] and X[1][1] and X[2][2]) or (X[0][2] and X[1][1] and X[2][0]):
      print("Yes")
    else:
      print("No")