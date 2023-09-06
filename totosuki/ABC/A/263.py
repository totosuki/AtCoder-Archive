ABCDE = list(map(int, input().split()))
nodupe = list(set(ABCDE))
flag = False
if len(nodupe) == 2:
  if ABCDE.count(nodupe[0]) == 2:
    if ABCDE.count(nodupe[1]) == 3:
      print("Yes")
      flag = True
  if ABCDE.count(nodupe[0]) == 3:
    if ABCDE.count(nodupe[1]) == 2:
      print("Yes")
      flag = True

if not flag:
  print("No")