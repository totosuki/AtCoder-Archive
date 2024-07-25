S = input()
for i in range(len(S)):
  if i%2==0:
    if S[i]=="L":
      print("No")
      break
  else:
    if S[i]=="R":
      print("No")
      break
else:
  print("Yes")