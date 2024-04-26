import re
S = input()
if re.fullmatch(r"A[a-z]{1}[a-z]*C[a-z]*[a-z]{1}",S):
  print("AC")
else:
  print("WA")