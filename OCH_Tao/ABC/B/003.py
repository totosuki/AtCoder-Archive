S = input()
T = input()
L = ["a","t","c","o","d","e","r"]
flag = True

for i in range(len(S)):
  if S[i] == T[i]:
    continue
  elif S[i] == "@":
    if T[i] in L:
      continue
    else:
      flag = False
  elif T[i] == "@":
    if S[i] in L:
      continue
    else:
      flag = False
  else:
    flag = False

if flag:
  print("You can win")
else:
  print("You will lose")