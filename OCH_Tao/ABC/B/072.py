S = list(input())
l = []
for i in range(len(S)):
  if i%2==0:
    l.append(S[i])
print("".join(l))