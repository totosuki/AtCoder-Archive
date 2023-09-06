S = input()
check_set = set()
for s in S:
  if s not in check_set:
    check_set.add(s)
  else:
    print("no")
    exit()
print("yes")