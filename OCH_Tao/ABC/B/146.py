X = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = int(input())
S = input()
Y = X[N:]+X[:N]
L = []
for i in range(len(S)):
  L.append(Y[X.index(S[i])])
print("".join(L))