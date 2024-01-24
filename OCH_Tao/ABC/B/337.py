S = list(input())
while len(S)>0 and S[0]=="A":
  S.pop(0)
else:
  while len(S)>0 and S[0]=="B":
    S.pop(0)
  else:
    while len(S)>0 and S[0]=="C":
      S.pop(0)

if S:
  print("No")
else:
  print("Yes")