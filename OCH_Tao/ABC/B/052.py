N = int(input())
S = list(input())
l = [0]
for i in S:
  if i == "I":
    l.append(l[-1]+1)
  else:
    l.append(l[-1]-1)
print(max(l))