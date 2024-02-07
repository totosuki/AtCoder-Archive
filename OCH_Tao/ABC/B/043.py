S = list(input())
l = []
for i in S:
  if i == "B":
    if l!=[]:
      l.pop()
  else:
    l.append(i)
print("".join(l))