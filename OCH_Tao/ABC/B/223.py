S = input()
L = []
for i in range(len(S)):
  L.append(S[i:]+S[:i])
print(min(L))
print(max(L))