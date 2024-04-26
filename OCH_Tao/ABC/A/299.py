import re
N = int(input())
S = input()
if re.search(r'\|.*\*.*\|',S):
  print("in")
else:
  print("out")