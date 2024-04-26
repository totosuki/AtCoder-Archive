import re
S = input()
if re.fullmatch(r"<(=)+>",S):
  print("Yes")
else:
  print("No")