O = list(input())
E = list(input())
l = []
for i in range(len(O)):
  l.append(O[i])
  if len(O)-len(E)==1 and i==len(O)-1:
    break
  else:
    l.append(E[i])
print("".join(l))