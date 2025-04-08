# S = input()
# if (S.index("R") < S.index("K") < S.rindex("R")) and (S.index("B") % 2 != S.rindex("B") % 2):
#   print("Yes")
# else:
#   print("No")
import re
S = input()
if re.match(r".*R.*K.*R.*", S) and re.match(r".*B(..)*B.*", S):
  print("Yes")
else:
  print("No")
