N = input()
l = []
for i in range(len(N)):
  if N[i]=="1":
    l.append("9")
  elif N[i]=="9":
    l.append("1")
  else:
    l.append(N[i])
print("".join(l))