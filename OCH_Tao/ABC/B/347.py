S = input()
L = set()
for i in range(len(S)+1):
  for j in range(i+1,len(S)+1):
    L.add(S[i:j])
print(len(L))