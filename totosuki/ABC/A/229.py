S1 = input()
S2 = input()
if (S1[0]+S2[0] == "##") or (S1[1]+S2[1] == "##"):
  print("Yes")
elif S1 == "##" or S2 == "##":
  print("Yes")
else:
  print("No")