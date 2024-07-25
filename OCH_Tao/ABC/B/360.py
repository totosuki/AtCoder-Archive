S,T = input().split()
L = []
for i in range(1,len(S)):
  for j in range(i):
    L.append(S[j::i])
print("Yes" if T in L else "No")