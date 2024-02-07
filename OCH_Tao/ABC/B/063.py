S = input()
if len(S)!=len(list(set(S))):
  print("no")
else:
  print("yes")