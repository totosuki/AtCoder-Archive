import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase

S = input()

if S[0] in upper:
  flag = True
  for s in S[1:]:
    if s not in lower:
      flag = False
  if flag:
    print("Yes")
  else:
    print("No")
else:
  print("No")