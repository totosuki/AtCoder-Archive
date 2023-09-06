S = input()
S_kinds = len(set(list(S)))
if S_kinds == 1:
  print(1)
elif S_kinds == 2:
  print(3)
else:
  print(6)