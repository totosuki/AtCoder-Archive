N = input()
L = ["000","111","222","333","444","555","666","777","888","999"]
if N[0:3] in L:
  print("Yes")
elif N[1:] in L:
  print("Yes")
else:
  print("No")